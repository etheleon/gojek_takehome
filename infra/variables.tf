variable "gke_project" {
  description = "The project name which the K8S cluster be provisioned under"
  default = "datascience"
}

variable "gke_region" {
  description = "Region which the K8S cluster be provisioned in"
  default = "asia-southeast1-b"
}
