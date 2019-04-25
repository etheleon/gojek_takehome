## Precompute

The µservice serves 3 endpoints, each of which requires a precompute to be done and saved to GCS. 

We initially carried out the extraction in Jupyter, the notebook is found at [precompute/API.ipynb](../precompute/API.ipynb)


Each precompute is done by a python script. 

| API | Description |
| --- | --- |
| Total Trips | [precompute/total_trips.py](../precompute/total_trips.py) |
| Fare Heatmeap | [precompute/fare_heatmap](../precompute/fare_heatmap.py) |
| Average Speed | [precompute/average_speed](../precompute/average_speed.py) |

We have also created a [utilities](../precompute/gojek/util) python module. 

Once the cleaned data is computed, the next step is to start serving them as a service. 

Next: [Installing µservice as a helm package into cluster](03-helm-chart.md)
