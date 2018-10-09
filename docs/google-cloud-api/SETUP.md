Google Cloud
------------

https://cloud.google.com/compute/docs/tutorials/python-guide

1. [Create a Google Cloud Platform project](https://console.cloud.google.com/cloud-resource-manager)

2. [Make sure billing is enabled for your project](https://console.cloud.google.com/billing/)

3. [Install the Google Cloud SDK](https://cloud.google.com/sdk/)

4. Run `gcloud auth application-default login`.

5. Install the google-api-python-client](): 

````
pip install --upgrade google-api-python-client
````

6. [Enable the Google Cloud Storage API](https://support.google.com/cloud/answer/6158841?hl=en&ref_topic=6262490)

7. [Create a storage bucket](https://cloud.google.com/storage/docs/creating-buckets)

8. [Setup application credentials](https://developers.google.com/accounts/docs/application-default-credentials)

9. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your application credentials file.
