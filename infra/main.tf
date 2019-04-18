resource "google_container_cluster" "gojek" {
	name               = "${var.gke_cluster_name}"
	network            = "default"
	location               = "${var.gke_region}"

  remove_default_node_pool = true
	initial_node_count = 1

	#disable basic auth
	master_auth {
		username = ""
		password = ""
	}
}

resource "google_container_node_pool" "main_pool" {
	name       = "normal"
	location   = "${var.gke_region}"
	cluster    = "${google_container_cluster.gojek.name}"
	node_count = 1

	node_config {
		preemptible  = true
		machine_type = "n1-standard-1"

		metadata {
			disable-legacy-endpoints = "true"
		}

		oauth_scopes = [
			"https://www.googleapis.com/auth/logging.write",
			"https://www.googleapis.com/auth/monitoring",
		]
	}
}

resource "google_container_node_pool" "gpu_pool" {
	name               = "gpu"
	location               = "${var.gke_region}"
	cluster            = "${google_container_cluster.gojek.name}"
	initial_node_count = 0
	autoscaling {
		min_node_count = 0
		max_node_count = 3
	}
	# number of GPUs attached to each instance
  node_config{
    guest_accelerator {
      type  = "nvidia-tesla-p4"
      count = 1
    }
  }
}

