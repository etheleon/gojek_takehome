terraform {
  backend "gcs" {
    bucket  = "terraform-remote-state-storage-gb"
    project = "datascience-237903"
    credentials = "./creds/serviceaccount.json"
  }
}

resource "google_storage_bucket" "gojek-geoapi-assets" {
  name     = "geoapi-assets"
}

resource "google_compute_address" "ip_address" {
  name = "gojek-ip"
}

resource "google_container_cluster" "gojek" {
	name               = "${var.gke_cluster_name}"
	network            = "default"
	location               = "${var.region}"

  remove_default_node_pool = true
	initial_node_count = 1

  master_auth {
    username = ""
    password = ""
  }

  min_master_version = "${var.k8s-version}"
}

resource "google_container_node_pool" "main_pool" {
	name       = "normal"
	location   = "${var.region}"
	cluster    = "${google_container_cluster.gojek.name}"
	node_count = 1
	autoscaling {
		min_node_count = 1
		max_node_count = 3
	}

	version = "${var.k8s-version}"

	node_config {
		preemptible  = true
		machine_type = "n1-standard-1"

		metadata {
			disable-legacy-endpoints = "true"
		}

		oauth_scopes = [
			"https://www.googleapis.com/auth/logging.write",
			"https://www.googleapis.com/auth/monitoring",
			"https://www.googleapis.com/auth/compute",
			"https://www.googleapis.com/auth/devstorage.read_only",
		]
	}
}

resource "google_container_node_pool" "compute_pool" {
	name               = "compute"
	location           = "${var.region}"
	cluster            = "${google_container_cluster.gojek.name}"
	initial_node_count = 0
	autoscaling {
		min_node_count = 0
		max_node_count = 3
	}

  version = "${var.k8s-version}"

  node_config{
    machine_type = "n1-highmem-16"
  }

  oauth_scopes = [
    "https://www.googleapis.com/auth/logging.write",
    "https://www.googleapis.com/auth/monitoring",
    "https://www.googleapis.com/auth/compute",
    "https://www.googleapis.com/auth/devstorage.read_only",
  ]
}

resource "google_container_node_pool" "gpu_pool" {
	name               = "gpu"
	location               = "${var.region}"
	cluster            = "${google_container_cluster.gojek.name}"
	initial_node_count = 0
	autoscaling {
		min_node_count = 0
		max_node_count = 3
	}

  version = "${var.k8s-version}"

  node_config{
    guest_accelerator {
      type  = "nvidia-tesla-p4"
      count = 1
    }
  }

  oauth_scopes = [
    "https://www.googleapis.com/auth/logging.write",
    "https://www.googleapis.com/auth/monitoring",
    "https://www.googleapis.com/auth/compute",
    "https://www.googleapis.com/auth/devstorage.read_only",
  ]
}
