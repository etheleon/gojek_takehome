## Precompute

The µservice serves 3 endpoints, each of which requires a precompute to be done and saved to GCS. Each precompute is done by a python script. 

| API | Description |
| Total Trips | [total_trips.py](../precompute/total_trips.py) |
| Fare Heatmeap | [fare_heatmap](../precompute/fare_heatmap.py) |
| Average Speed | [average_speed](../precompute/average_speed.py) |

We have also created a [utilities](../precompute/gojek/util) python module. 

Once the clean data is ready it's time to start serving these services. 

Next: [Installing µservice as a helm package into cluster](03-helm-chart.md)
