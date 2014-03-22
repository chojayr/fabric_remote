# Fabric Remote

A HTTP Rest API to Fabric.

## Requirements
Fabric Remote is written in Flask and requires Fabric to be installed.

Just set the FABFILE config variable to point to your Fabfile.  This is the filesystem path, not the python module path.
### Get Task List

`GET /tasks` returns list of tasks

### Execute Task

Send a POST request to the server with the task and args you will execute in the body.  Make sure you set the Content-Type header to application/json.  

`POST /executions body -> [{task: "deploy", args: ["foo", "bar"], kwargs: {"arg1":"val1"}}]`

If this works, it will return 202 Accepted with a json response body containing two other endpoints: results and output.  

```json
{
    "output":"/executions/1234-1234-12345/output",
    "results":"/executions/1234-1234-12345/results",
}
```

The output endpoint will stream the output of the fabric task as it runs.  After the task completes, it will contain the full output of the task.

The results task will return a json response:

```json
{
    "error": "",
    "finished": true,
    "results": [ ]
}
```

`error` contains the error message if there was an error executing your task, `finished` returns the current state of the task, and `results` is a list of all the return values of the tasks you ran.

## Installation
1. `pip install fabric-remote`

## Notes
Fabric Remote is only compatible with "new-style" Fabfiles (introduced in Fabric 1.1).  It doesn't know how to deal with "old-style" tasks that don't use the @task decorator or aren't subclasses of the Task object.
