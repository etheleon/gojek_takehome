# Introduction

Helm is the defacto package manager for K8S clusters

Once you've run `terraform apply`, it's time now to install `helm` and `tiller`

![diagram](https://d1qy7qyune0vt1.cloudfront.net/nutanix-us/attachment/fa2af93e-44da-4ba4-a8b4-e39215f61a03.png)

## Step 1: Install Helm (Client)

* Download installer 

    ```
    curl_status=$(curl -w '%{http_code}\n' https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get -o get_helm.sh)
    chmod a+x get_helm.sh
    ```
    
* Run installstaller

    ```
    bash get_helm.sh
    ```


## Step 2: Install Tiller (server)

* Set up service account and bind cluster role

    ```
    kubectl create serviceaccount --namespace kube-system tiller

    kubectl create clusterrolebinding tiller-cluster-rule \
	    --clusterrole=cluster-admin \
    	    --serviceaccount=kube-system:tiller
    ```

* Run patch

    ```
    kubectl patch deploy --namespace kube-system tiller-deploy \
	    -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
    ```
    
* Install tiller

    ```
    helm init
    ```


## Step 3: Install helm chart

Run the following from the [helm-charts](../helm-charts) directory

```
RELEASE_NAME=gojek
helm install -n $RELEASE_NAME geoapi
```


Next: [CI/CD Updating the µservice](04-ci_cd.md)
