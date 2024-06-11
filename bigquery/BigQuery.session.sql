WITH trips_selected AS (
  SELECT
    EXTRACT(DAYOFWEEK FROM TIMESTAMP(start_date)) AS weekday,
    EXTRACT(YEAR FROM TIMESTAMP(start_date)) AS year,
    duration_sec
  FROM
    `bigquery-public-data.san_francisco.bikeshare_trips`
)

SELECT
  weekday,
  AVG(CASE WHEN year = 2016 THEN duration_sec END) AS average_duration_2016,
  SUM(duration_sec) AS total_duration
FROM
  trips_selected
GROUP BY
  weekday
ORDER BY
  total_duration DESC
limit 1