# flask-openwhisk

An experimental integration of Flask on OpenWhisk

## How to Use

Currently there is a single function called `invoke` that will translate a raw
HTTP request from OpenWhisk into a WSGI/Flask request and then back into an
OpenWhisk response.

You just need to create the main program (`__main__.py`) that looks like the
following:

```python
from flaskwsk.handle import invoke
from web import app

def main(args):
   return invoke(app,args)
```

In the above `app` is the Flask application object.

To package you need to include in the zip file:

 1. The `virtualenv` with all the packaged you Use
 2. The invocation including the `__main__.py` file

Then you create a raw HTTP action:

```bash
wsk action create myapp --kind python:3 myapp.zip --web raw
```

## An Example

The makefile will package a deploy an example application that just echoes a
request:

To build and deploy:

```bash
make setup
make
make create
```

To test:

```bash
curl  -v -X PUT -d "test" -H "Content-Type: text/plain" http://$APIHOST/api/v1/web/flask/echo
```

and you should see output like:

```json
{
  "data": "test",
  "headers": {
    "Accept": "*/*",
    "Connection": "close",
    "Content-Length": "4",
    "Content-Type": "text/plain",
    "Host": "n.n.n.n:10001",
    "User-Agent": "curl/7.53.1",
    "Via": "1.1 DQAAABxhMzM-"
  },
  "method": "PUT"
}
```
