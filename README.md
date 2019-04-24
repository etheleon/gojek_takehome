> Repository storing the codebase required for the takehome test (2weeks)

# Takehome Solution
The intructions for this takehome test can be found in the [INSTRUCTIONS.md](./INSTRUCTIONS.md) file.

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

# FAQ

Any questions, please forward them to Wesley at etheleon@protonmail.com.
