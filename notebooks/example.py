""" Download data
"""

from gojek.util.db import get_dataframe_from_bigquery

def get_tables():
    """
    >>> get_tables()
    """
    # Green taxis
    greens = "tlc_green_trips_{YEAR}"
    tables = [greens.format(YEAR=year) for year in [2014, 2015, 2016, 2017]]
    # Yellow taxis
    yellows = "tlc_yellow_trips_{YEAR}"
    tables.extend([yellows.format(YEAR=year) for year in [2015, 2016, 2017]])
    table_str = "bigquery-public-data.new_york_taxi_trips.{TABLE}"
    return [table_str.format(TABLE=table) for table in tables]

tables = get_tables()

query = '''SELECT *
    FROM `{TABLE}`
    LIMIT 5
    '''
df1 = get_dataframe_from_bigquery(query.format(TABLE=tables[0]))
df1

query = '''SELECT
            cast(pickup_datetime AS date) AS date,
            pickup_latitude,
            pickup_longitude,
            total_amount
        FROM
            `{TABLE}`
        '''
query = query.format(TABLE=tables[4])

df2 = get_dataframe_from_bigquery(query.format(TABLE=tables[4]), is_big=True)
