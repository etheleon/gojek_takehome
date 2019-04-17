
# Get Service Account Credentials

Download the service account credentials:

1. Go to `APIs & Services`

   ![iam](https://i.imgur.com/V4tnrfn.png)

2. Set the following parameters:
    * __service account name__: `terraform`
    * __role__: `project > editor`
    * __key type__: `JSON`
    ![generate_creds](https://i.imgur.com/NPhMmNS.png)


3. _Download_ credentials file as `serviceaccount.json` in `creds` dir
4.  _Export_ the following to your `~/.zshrc` or `~/.bashrc`.

   ```
   export GOOGLE_CLOUD_KEYFILE_JSON=<creds.json>
   ```
