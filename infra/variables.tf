variable "gke_project" {
  description = "The project name which the K8S cluster be provisioned under"
  default = "datascience-237903"
}

variable "gke_region" {
  description = "Region which the K8S cluster be provisioned in"
  default = "asia-southeast1-b"
}

variable "gke_cluster_name" {
  description = "K8S cluster name"
  default = "altimit"
}

variable "k8s-version" {
  default     = "1.11"
  type        = "string"
  description = "Required K8s version"
}
