resource "google_container_cluster" "gojek" {
	name               = "${var.gke_cluster_name}"
	network            = "default"
	location               = "${var.gke_region}"

  remove_default_node_pool = true
	initial_node_count = 1

  master_auth {
    username = "altimit"
    password = "pvuCWQokALeyUQ2zWU4yEqJz"
  }

  enable_legacy_abac = true
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
      "https://www.googleapis.com/auth/compute",
      "https://www.googleapis.com/auth/devstorage.read_only",
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

data "template_file" "kubeconfig" {
  template = "${file("${path.module}/kubeconfig-template.yaml")}"

  vars {
    context = "gojek"
    cluster_name    = "${google_container_cluster.gojek.name}"
    user_name       = "${google_container_cluster.gojek.master_auth.0.username}"
    user_password   = "${google_container_cluster.gojek.master_auth.0.password}"
    endpoint        = "${google_container_cluster.gojek.endpoint}"
    cluster_ca      = "${google_container_cluster.gojek.master_auth.0.cluster_ca_certificate}"
    client_cert     = "${google_container_cluster.gojek.master_auth.0.client_certificate}"
    client_cert_key = "${google_container_cluster.gojek.master_auth.0.client_key}"
  }
}

resource "local_file" "kubeconfig" {
  content  = "${data.template_file.kubeconfig.rendered}"
  filename = "${path.module}/kubeconfig"
}
