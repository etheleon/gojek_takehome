## Precompute

The µservice serves 3 endpoints, each of which requires a precompute to be done and saved to GCS.

We initially carried out the extraction in Jupyter, the notebook is found at [precompute/APIs.ipynb](../precompute/APIs.ipynb)


Each precompute is done by python script gojek which is installed by the python package [gojek](../precompute/gojek)

You would run 

```
$ gojek [average-speed fare-heatmaps tables trips-per-day]
```

```bash
export SETTINGS_FILE_FOR_DYNACONF=/work/github/gojek_takehome/precompute/config/settings.py
```

Once the cleaned data is computed, the next step is to start serving them as a service.

Next: [Installing µservice as a helm package into cluster](03-helm-chart.md)
