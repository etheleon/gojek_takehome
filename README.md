> Repository storing the codebase required for the takehome test (2weeks)

# Takehome Solution

The intructions for this takehome test can be found in the [INSTRUCTIONS.md](./INSTRUCTIONS.md) file.


<!-- vim-markdown-toc GFM -->

  * [Folder Organisation](#folder-organisation)
  * [Getting Started](#getting-started)
  * [Endpoints](#endpoints)
      * [1. Swagger](#1-swagger)
      * [2. heartbeat](#2-heartbeat)
      * [3. Total Trips](#3-total-trips)
      * [4. Fare Heatmap](#4-fare-heatmap)
      * [5. Average Speed](#5-average-speed)
* [FAQ](#faq)

<!-- vim-markdown-toc -->

## Folder Organisation

Starting with the root directory, you will find several folders:

* `terraform` necessary scripts to recreate infrastructure eg. GKE cluster.
* `helm-charts` µservice as an installable app using K8S's de-facto package manager _helm_ (similar to brew but for installing into K8S clusters)
* `precompute` Contains the scripts to generate the data served by the APIs
* `notebook` stores EDA notebook
* `components` source for the different components required for the app, currently it's just one `geoapi` a flask app, possible to extend this further for other resources eg. cache, db, etc

As well as standalone files:

* [cloudbuild.yaml](./cloudbuild.yaml) for build instructions; publishing images to GCR and installing the latest package
* [INSTRUCTIONS.md](./INSTRUCTIONS.md) which stores the takehome's instructions

## Getting Started

Read the [installation guide](./docs/00-introduction.md) for instructions on setting up the microservice on Google Cloud Platform.

## Endpoints

  ### Port Forwarding

To test the APIs you can use `kubectl` to port forward the service:

  ```bash
  kubectl port-forward svc/gojek-microservice-geoapi 5000:80
  ```

  > **NOTE**: Set `KUBECONFIG` ENV VAR as the path where `.kubeconfig` (included in submission email).


#### 1. Swagger

  [Swagger docs](https://swagger.io/docs/specification/2-0/what-is-swagger/) can be found hosted at the following endpoint [/v1/docs](localhost:5000/v1/docs)

#### 2. heartbeat

  Livenes and Readiness probes are pointed at this endpoint

  ```bash
  curl localhost:5000/heartbeat
  ```

#### 3. Total Trips


  Returns the #trips for a given day

  ```bash
  START_DATE=2015-01-01
  END_DATE=2015-03-01

  curl "localhost:5000/v1/total_trips?start=${START_DATE}&end=${END_DATE}"
  ```

#### 4. Fare Heatmap

  Returns the average fare in a given S2 Cell

  ```bash
  DATE=2015-01-01

  curl "localhost:5000/v1/average_fare_heatmap?date=${DATE}"
  ```

#### 5. Average Speed

  Returns the average speed for a given day

  ```bash
  DATE=2015-01-01

  curl "localhost:5000/v1/average_speed_24hrs?date=${DATE}"
  ```

# FAQ

Any questions, please forward them to Wesley at etheleon [at] protonmail [dot] com.
