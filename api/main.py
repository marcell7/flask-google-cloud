import os
import json
import time
from flask import Flask, request
from google.cloud import tasks_v2


app = Flask(__name__)
client = tasks_v2.CloudTasksClient()

PROJECT_ID = "Your Google Cloud project name"
LOCATION_ID = "Server location"
QUEUE_ID = "Name of the task queue"
SERVICE_ACCOUNT_EMAIL = "Service account that can invoke cloud functions and has permissions to add tasks to task queue"
FUNCTION_URL = "URL of the cloud function"


@app.route("/", methods=["POST"])
def hello_world():
    """Example Hello World route."""
    data = request.get_json()
    return f"Hello {data['name']}!"

@app.route("/create-task", methods=["POST"])
def create_task():
    data = request.get_json()
    n = data["n"]

    # Adds a task to Cloud Tasks queue
    task = tasks_v2.Task(
        http_request=tasks_v2.HttpRequest(
            http_method=tasks_v2.HttpMethod.POST,
            url=FUNCTION_URL,
            oidc_token=tasks_v2.OidcToken(
                service_account_email=SERVICE_ACCOUNT_EMAIL
            ),
            headers={"Content-type": "application/json"},
            body=json.dumps({"n": n}).encode(),
        ),
        name=(client.task_path(PROJECT_ID, LOCATION_ID, QUEUE_ID, str(time.time()).replace(".", "")))
    )

    client.create_task(
        tasks_v2.CreateTaskRequest(
            parent=client.queue_path(PROJECT_ID, LOCATION_ID, QUEUE_ID),
            task=task
        )
    )

    return {"status": "TASK CREATED SUCCESSFULLY"}




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))