"""Calculates fare heatmap
"""

import os
import gc
import subprocess
from tempfile import NamedTemporaryFile

from tqdm import tqdm

import pandas as pd

from gojek.util.db import get_dataframe_from_bigquery


QUERY_TEMPLATE = '''
    SELECT
        cast(pickup_datetime AS date) AS date,
        pickup_latitude,
        pickup_longitude,
        total_amount
    FROM
        `{TABLE}`
    WHERE
        pickup_latitude IS NOT NULL
        AND pickup_longitude IS NOT NULL
        AND total_amount IS NOT NULL
                '''


def get_tables():
    """
    >>> get_tables()
    """
# Green taxis
    greens = "tlc_green_trips_{YEAR}"
    green_years = [2014, 2015, 2016, 2017]
    tables = [greens.format(YEAR=year) for year in green_years]
# Yellow taxis
    yellows = "tlc_yellow_trips_{YEAR}"
    yellow_years = [2015, 2016, 2017]
    tables.extend([yellows.format(YEAR=year) for year in yellow_years])
    table_str = "bigquery-public-data.new_york_taxi_trips.{TABLE}"
    return pd.DataFrame({
        "tables": [table_str.format(TABLE=table) for table in tables],
        "year": green_years + yellow_years,
        "color": ["green" for i in green_years] +
                 ["yellow" for i in yellow_years]
    })


def compute_ave_fare(table, year, color):
    """downloads dataset"""
    temporary_file = NamedTemporaryFile().name
    temporary_file2 = NamedTemporaryFile().name
    query = QUERY_TEMPLATE.format(TABLE=table)
    df = get_dataframe_from_bigquery(query, is_big=True).compute()
    if df.shape[0] == 0:
        print("No rows in table satisfy query")
        return None
    df.dropna().to_csv(temporary_file, index=False)
    del df
    gc.collect()
    with open(temporary_file2, "w") as outfile:
        subprocess.call(["latlng2s2", temporary_file], stdout=outfile)
    print(f"Processed: {year} - {color} - {temporary_file}")
    (pd.read_csv("tmp5u5l5pdr", header=None,
                      names=["date", "s2id", "total_amount"])
          .groupby(["date", "s2id"])
          .mean()
          .dropna()
          .reset_index()
          .rename({"total_amount": "ave_fare"})
          .to_csv(f"{color}-{year}.csv.gz",
                  compression="gzip",
                  index=False))
    gc.collect()


if __name__ == '__main__':
    import time

    TABLES_DF = get_tables()

    for _, row in tqdm(TABLES_DF.query("color == 'yellow'").iterrows(), desc="Computed Tables"):
        try:
            tbl = row["tables"]
            yr = row["year"]
            col = row["color"]
            print(f"STARTING: {col} {yr}")
            start = time.time()
            compute_ave_fare(tbl, yr, col)
            end = time.time()
            taken = (end - start) / 60
            print(f"DONE: {col} {yr} | TIME: {taken} min")
        except Exception as err:
            print(f"{yr} {col} is weird")
            print(f"Exception: {err}")

# Computed Tables: 1it [04:57, 297.79s/it] DONE: green 2014 | TIME: 4.963149774074554 min
# Computed Tables: 2it [10:29, 307.94s/it]DONE: green 2015 | TIME: 5.527217908700307 min
# green 2016 is invalid

# Computed Tables: 1it [18:40, 1120.92s/it]Processed: 2015 - yellow - /tmp/tmponbnglbd
# 2015 yellow is weird

# Computed Tables: 2it [29:23, 977.36s/it] Processed: 2016 - yellow - /tmp/tmp5r83q7z_
# 2016 yellow is weird

# Computed Tables: 3it [29:45, 690.92s/it]No rows in table satisfy query
# DONE: yellow 2017 | TIME: 0.37569501797358196 min
