## Precompute

The µservice serves 3 endpoints, each of which requires a precompute to be done and saved to GCS. 

We initially carried out the extraction in Jupyter, the notebook is found at [precompute/API.ipynb](../precompute/API.ipynb)


Each precompute is done by a python script. 

| API | Description |
| --- | --- |
| Total Trips | [precompute/00-total_trips.py](../precompute/00-total_trips.py) |
| Fare Heatmeap | [precompute/01-fare_heatmap.py](../precompute/01-fare_heatmap.py) |
| Average Speed | [precompute/02-average_speed.py](../precompute/02-average_speed.py) |

We have also created a [utilities](../precompute/gojek/util) python module. Please install it before running any of the scripts above

Once the cleaned data is computed, the next step is to start serving them as a service. 

Next: [Installing µservice as a helm package into cluster](03-helm-chart.md)
