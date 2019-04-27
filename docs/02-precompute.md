## Precompute

The µservice serves 3 endpoints, each of which requires a precompute to be done and saved to GCS.

We initially carried out the extraction in Jupyter, the notebook is found at [precompute/APIs.ipynb](../precompute/APIs.ipynb)


Each precompute is done by a python script.

| API | Description |
| --- | --- |
| Total Trips | [precompute/00-total_trips.py](../precompute/00-total_trips.py) |
| Fare Heatmeap | [precompute/01-fare_heatmap.py](../precompute/01-fare_heatmap.py) |
| Average Speed | [precompute/02-average_speed.py](../precompute/02-average_speed.py) |

We have also created a small python module [gojek](../precompute/gojek/util). Please install it before running any of the scripts above

Also export the path of [settings.py](../precompute/config/settings.py):

```bash
export SETTINGS_FILE_FOR_DYNACONF=/work/github/gojek_takehome/precompute/config/settings.py
```

Once the cleaned data is computed, the next step is to start serving them as a service.

Next: [Installing µservice as a helm package into cluster](03-helm-chart.md)
