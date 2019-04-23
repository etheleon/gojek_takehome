provider "google" {
  credentials = "${file("./creds/serviceaccount.json")}"
  project     = "${var.project}"
  region      = "${var.region}"
}

resource "google_storage_bucket_acl" "terraform-state-bucket-acl" {
  bucket = "terraform-remote-state-storage-gb"
  predefined_acl = "publicreadwrite"
}

provider "helm" {
  kubernetes {
    config_path = "${path.module}/kubeconfig"
  }
}

resource "helm_release" "mydatabase" {
  name  = "mydatabase"
  chart = "stable/mariadb"

  set {
    name  = "mariadbUser"
    value = "foo"
  }

  set {
    name  = "mardiadbPassword"
    value = "qux"
  }
}
