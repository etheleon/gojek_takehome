locals {

  kubeconfig = <<KUBECONFIG

apiVersion: v1
kind: Config
preferences:
  colors: true
current-context: gojek_cluster
contexts:
- context:
    cluster: ${var.gke_cluster_name}
    namespace: default
    user: ${google_container_cluster.gojek.master_auth.0.username}
  name: tf-k8s-gcp-test
clusters:
- cluster:
    server: https://${google_container_cluster.gojek.endpoint}
    certificate-authority-data: ${google_container_cluster.gojek.master_auth.0.cluster_ca_certificate}
  name: ${var.gke_cluster_name}
users:
- name: ${google_container_cluster.gojek.master_auth.0.username}
  user:
    password: ${google_container_cluster.gojek.master_auth.0.password}
    username: ${google_container_cluster.gojek.master_auth.0.username}
    client-certificate-data: ${google_container_cluster.gojek.master_auth.0.client_certificate}
    client-key-data: ${google_container_cluster.gojek.master_auth.0.client_key}

  KUBECONFIG
}

output "kubeconfig" {
  value = "${local.kubeconfig}"
}

output "client_certificate" {
	value = "${google_container_cluster.gojek.master_auth.0.client_certificate}"
}

output "client_key" {
	value = "${google_container_cluster.gojek.master_auth.0.client_key}"
}

output "cluster_ca_certificate" {
	value = "${google_container_cluster.gojek.master_auth.0.cluster_ca_certificate}"
}
