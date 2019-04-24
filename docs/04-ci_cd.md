# Continuous Integration / Continuous Deployment

We will be using cloud build to achieve this process

You will have to allow access for cloudbuild kubectl to update the deployment's image:

```
PROJECT="$(gcloud projects describe \
    $(gcloud config get-value core/project -q) --format='get(projectNumber)')"

gcloud projects add-iam-policy-binding $PROJECT \
    --member=serviceAccount:$PROJECT@cloudbuild.gserviceaccount.com \
    --role=roles/container.developer
```

