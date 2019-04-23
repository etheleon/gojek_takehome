from etheleon/docker-alpine-python-machinelearning

COPY components/geoapi /geoapi
RUN pip install --no-cache-dir -r requirements/all.txt

CMD ["gunicorn", "-b", "0.0.0.0:5001", "--log-level", "info", "--pythonpath=/geoapp/app", "--timeout=120", "app:create_app()"]
