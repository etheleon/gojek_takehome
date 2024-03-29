# Introduction

This webservice is modelled closely after [12 Factor application](https://12factor.net).


## Local Environment setup


### Prerequisites

- [x] Python 3.6, Recommend using conda for easy installation.
- [x] PIP (comes with conda installation)

#### Setup environment

* Create virtual environment

	```bash
	conda create --name geoapi py=3.6
	source activate geoapi
	pip install -r requirements/all.txt
	```

### Getting Started

#### 1. ENV variables

| Variable | Description |
| --- | --- |
| `LOCAL_DIR` | path to this directory's `assets` folder |


#### 2. Run Application Server

* We will be using gunicorn as the applicatino server

	```bash
	gunicorn -b 0.0.0.0:5001 --pythonpath=$WORKDIR/app --timeout=120 "app:create_app()"
	```
