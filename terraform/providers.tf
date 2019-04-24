provider "google" {
  credentials = "${file("./creds/serviceaccount.json")}"
  project     = "${var.project}"
  region      = "${var.region}"
}

resource "google_storage_bucket_acl" "terraform-state-bucket-acl" {
  bucket = "terraform-remote-state-storage-gb"
  predefined_acl = "publicreadwrite"
}


