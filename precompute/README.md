# Introduction

To calculate the data to be served, install the package 

```
Usage:          gojek
                gojek average-speed
                gojek fare-heatmaps
                gojek trips-per-day
```


For more details read the [docs: 02-precompute.md](../docs/02-precompute.md).

```bash
docker run --rm \
  -v $CREDS:/creds \
  -v $SETTINGS:/settings \
  gcr.io/datascience-237903/gojek:compute \
  [trips_per_day | fare_heatmaps | average_speed ]
```
