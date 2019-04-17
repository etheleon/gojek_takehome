locals {

  kubeconfig = <<KUBECONFIG

  KUBECONFIG
}

output "kubeconfig" {
  value = "${local.kubeconfig}"
}

