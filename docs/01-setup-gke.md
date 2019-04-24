> The following README assumes you already have a billing account set up with GCP

# API infra

Terraform configuration for infrastructure. For a why and how of Terraform please refer this great series of blog posts and the official documentation


## Getting started


1. [Install](https://cloud.google.com/sdk/) `gcloud` CLI, authenticate
2. Enable API access to GCP `gcloud services enable compute.googleapis.com`
3. [Get serviceaccount credentials](./docs/get_credentials.json)
4. Setup Terraform:
	* [Download and install terraform](https://www.terraform.io/downloads.html)
	* Create google bucket to store tfstate file eg. `terraform-remote-state-storage-`
5. Clone Repository and run the following from the `./terraform` dir
gb`
6. Run `terraform init` to fetch providers
7. Run `terraform apply`


Read more here: https://cloud.google.com/community/tutorials/managing-gcp-projects-with-terraform

Next: [Precomputing the serving data](02-precompute.md)