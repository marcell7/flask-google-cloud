Command to deploy function on Google Cloud functions (with parameters I've used)
``gcloud functions deploy python-http-function --gen2 --runtime=python311 --region=europe-west3 --source=. --entry-point=sleep_for --trigger-http --allow-unauthenticated``


Be careful when configuring permissions for the deployed function. The command above makes it accessible by all users.
For authenticated access make sure to read the [documentation](https://cloud.google.com/tasks/docs/creating-http-target-tasks#sa).
