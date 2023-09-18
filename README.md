## Deploy Flask api to Google Cloud (Cloud run + Cloud functions + Cloud Tasks)
The most basic setup to get Flask api working on Google Cloud. Api is running on Cloud run. It exposes /create-task endpoint that adds tasks to task queue running on Cloud Tasks. Those tasks are then processed by a function running on Cloud Functions.

I'm sharing this mainly because documentation on this is not that great and all over the place...and also for future reference.
