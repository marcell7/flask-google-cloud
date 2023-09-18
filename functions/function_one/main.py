import functions_framework
import time

@functions_framework.http
def sleep_for(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP function_one` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    data = request.get_json()
    n = int(data["n"])
    time.sleep(n)

    print(f"Slept for {n} seconds")
    return f"Slept for {n} seconds"
