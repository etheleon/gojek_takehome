output "cluster_name" {
  value = "${google_container_cluster.gojek.name}"
}

output "primary_zone" {
  value = "${google_container_cluster.gojek.zone}"
}

output "master_version" {
  value = "${google_container_cluster.gojek.min_master_version}"
}

output "main_pool_version" {
  value = "${google_container_node_pool.main_pool.version}"
}

output "gpu_pool_version" {
  value = "${google_container_node_pool.gpu_pool.version}"
}

output "compute_pool_version" {
  value = "${google_container_node_pool.compute_pool.version}"
}
