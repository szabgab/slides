# Exercise: Simple Single-user TODO list API


* Write a web application that serves JSON files. Create the following end-points:
* `/api/add/Task to do`        will store the "Task to do" in a "database" and if successful it will return:

```
{"status": "ok", elapsed: "0.00003", id: "13124"}
```

* `/api/list`                  will return the list of all the items with their id: { "items": [ { "text": "Task to do", "id": "13124" }, { "text": "Other thing", "id" : "7238" }], elapsed: "0.0004", "status": "ok" }
* `/api/get/ID                 will return the given task from the database. Will return {"text": "Task to do", "id": "13124", "status": "ok"} if ID was 13124, will return {"status": "failure"} if failed. (e.g. the item was not in the database) set HTTP code to 404 if no such ID found.
* `/api/del/ID                 will remove the given task from the database. Will return {"status": "ok"} if managed to remove, will return {"status": "failure"} if failed. (e.g. the item was not in the database)

* `elapsed` is the time the operation took
* `id` is some unique id for the task
* `status` can be `ok` or `failure`



