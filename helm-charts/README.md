# Introduction

Helm is the defacto package manager for K8S clusters

Once you've run `terraform apply`, it's time now to install `helm` and `tiller`

![diagram](https://d1qy7qyune0vt1.cloudfront.net/nutanix-us/attachment/fa2af93e-44da-4ba4-a8b4-e39215f61a03.png)

Step 1: Download `get_helm.sh` scriptx

```
curl_status=$(curl -w '%{http_code}\n' https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get -o get_helm.sh)
chmod a+x get_helm.sh
```

```
helm init
```