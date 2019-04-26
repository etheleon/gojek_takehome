"""Calculates fare heatmap
"""

import logging

import pandas as pd

from gojek.util.geo import compute_ave_fare


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


if __name__ == '__main__':

    LOGGER = logging.getLogger("geo")
    LOGGER.setLevel(logging.DEBUG)

    TABLES_DF = get_tables()
    VALIDS = []
    for _, row in TABLES_DF.iterrows():
        try:
            tbl, yr, col = row["tables"], row["year"], row["color"]
            compute_ave_fare(tbl, yr, col)
            VALIDS.append(f"{col}-{yr}.csv.gz")
        except Exception as err:  # pylint: disable=broad-except
            LOGGER.warning(f"Error {yr}-{col}: {err}")

    (pd.concat([pd.read_csv(csv, compression="gzip") for csv in VALIDS])
     .groupby(["date", "s2id"])
     .mean()
     .reset_index()
     .to_csv("fare_heatmap.csv.gz",
             index=False,
             compression="gzip"))
