provider "google" {
  credentials = "${file("./creds/serviceaccount.json")}"
  project     = "${var.gke_project}"
  region      = "${var.gke_region}"
}
