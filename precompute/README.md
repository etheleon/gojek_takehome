# Introduction

To calculate the data to be served, install the [package: gojek](./gojek)

## Running this locally

```
Usage:          gojek
                gojek average-speed
                gojek fare-heatmaps
                gojek trips-per-day
```

## Docker

```bash
docker run --rm \
  -v $CREDS:/creds \
  -v $SETTINGS:/settings \
  gcr.io/datascience-237903/gojek:compute \
  [trips_per_day | fare_heatmaps | average_speed ]
```


ENV Variables

* `SETTINGS` points to the folder storing [settings.py](./config/settings.py)
* `CREDS` point to serviceaccount.json belonging to your GCP account
