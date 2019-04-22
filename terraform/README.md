> The following README assumes you already have a billing account set up with GCP

# API infra

Terraform configuration for infrastructure. For a why and how of Terraform please refer this great series of blog posts and the official documentation


## Getting started


1. [Download and install terraform](https://www.terraform.io/downloads.html)
2. Git clone this repository and cd into this directory
3. Ensure you have `gcloud` CLI to connect to the needed account ([Download Link](https://cloud.google.com/sdk/))
4. [Get serviceaccount credentials](./docs/get_credentials.json)
5. Create google bucket `terraform-remote-state-storage-gb`
5. Run `terraform init` in this folder
5. Run `terraform apply`

    ```
    terraform apply \
		-var 'region=asia-southeast1b' \
		-var 'username=MySecretUsername' \
		-var 'password=MySecretPassword'
    ```

Read me here: https://cloud.google.com/community/tutorials/managing-gcp-projects-with-terraform

## Contribution

Whenever you're making changes, try out


# Setting up Google CLI

Do step 0 only if you have configure gcloud previously ie. multiple GCP projects / accounts

* __Step 0: Login__

# Setting up Google CLI

    ```
    $ gcloud auth login --no-launch-browser
    ```

    Follow link to authenticate


## Google Cloud Platform Accounts

If you have multiple GCP accounts

* __Step 1: Configure gcloud CLI__

	* Create alternative configuration:

        ```bash
        $ ALIAS=gojek
        $ CONFIG_FILE=config_${ALIAS}
        $ vim $HOME/.config/gcloud/configurations/${CONFIG_FILE}
        ```

    * Include `<email>` and `<project-id>`

        ```
        [core]
	     account = <email>
	     project = <project-id>
        ```
    > **NOTE**: Original config would be found in `config_default`.

    * Switch Accounts

        ```bash
        $ gcloud config configurations activate gojek
        ```

* __Step 4: Create Project__

	* Create project

    ```
    gcloud projects create <your>-dl --enable-cloud-apis
    ```

	* Set project

	```
	gcloud config set project  <your>-dl
	```

* __Step 5: Enable API__

	* enable cloud api

	```
	gcloud services enable compute.googleapis.com

	```



## Repository Overview



## Top Level Structure



## Configuration


