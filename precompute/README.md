# Introduction

To calculate the data to be served, we use the following scripts:

` 00-total_trips.py`
` 01-fare_heatmap.py`
` 02-average_speed.py`

For more details read the [docs: 02-precompute.md](../docs/02-precompute.md).

```bash
docker run --rm \
  -v $CREDS:/creds \
  -v $settings:/settings \
  gcr.io/${PROJECT_ID}/gojek:compute
	[ trips_per_day | fare_heatmaps | average_speed ]
```
