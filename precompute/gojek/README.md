> Utilities package for takehome test

## Introduction

The package is used for computing input data for the geo API.

Before running the module please remember to set the ENV variable `SETTINGS_FILE_FOR_DYNACONF` to point to `settings.py`

## Local Environment setup

### Prerequisites

- [x] Python 3.6, Recommend using conda for easy installation.
- [x] PIP (comes with conda installation)

#### Setup environment

* Create virtual environment

	```bash
	conda create --name geoapi py=3
	source activate geoapi
	pip install -r requirements/all.txt
	```
  
### Installing the module

Run the following command from this directory

```bash
python setup.py install
```



