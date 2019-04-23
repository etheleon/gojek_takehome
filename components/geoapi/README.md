# Introduction

The webservice is closely modelled after [12 Factor application](https://12factor.net).

```
export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/client_secret.json'
```

Running the application

```bash
gunicorn -b 0.0.0.0:5001 --pythonpath=$WORKDIR/app --timeout=120 "app:create_app()"
```
