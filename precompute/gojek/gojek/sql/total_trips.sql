WITH num_pickups as (
    SELECT
    CAST(pickup_datetime AS date) AS date,
    COUNT(*)  AS total_trips,
    {YEAR}    AS year,
    '{COLOR}' AS color
FROM
    `{TABLE}`
GROUP BY CAST(pickup_datetime AS date)
)
SELECT
  *
FROM
  num_pickups
ORDER BY
  date
