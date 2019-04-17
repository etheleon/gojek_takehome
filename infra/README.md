> The following README assumes you already have a billing account set up with GCP

# API infra

Terraform configuration for infrastructure. For a why and how of Terraform please refer this great series of blog posts and the official documentation


## Getting started


1. [Download and install terraform](https://www.terraform.io/downloads.html)
2. Git clone this repository and cd into this directory
3. Ensure you have `gcloud` CLI to connect to the needed account ([Download Link](https://cloud.google.com/sdk/))
4. [Get serviceaccount credentials](./docs/get_credentials.md)
4. Run `terraform init` in this folder

## Google Cloud Platform Accounts

If you have multiple GCP accounts

* __Step 1: Configure gcloud CLI__

	* Create alternative configuration: 
	
        ```bash
        $ ALIAS=gojek
        $ CONFIG_FILE=config_${ALIAS}
        $ vim $HOME/.config/gcloud/configurations/${CONFIG_FILE}
        ```
    

    * Include account `<email>` and project's `<projectname>` 

        ```
        [core]
	     account = <email>
	     project = <projectname>
        ```
    
    > Original config would be found in `config_default`.

    * Switch Accounts

        ```bash
        $ gcloud config configurations activate gojek
        ```
        
* __Step 3: Login__

    ```
    $ gcloud auth login
    ```
    
    This will open a browser asking you to authenticate
    

## Repository Overview

## Top Level Structure

## Configuration

