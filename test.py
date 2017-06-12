from flaskwsk import invoke
from web import app
from base64 import b64encode, b64decode

get = {
   '__ow_method' : 'GET',
   '__ow_headers' : {},
   '__ow_path' : '/echo'
}

data = 'Hello World!'.encode('utf-8')
post = {
   '__ow_method' : 'POST',
   '__ow_headers' : {
      'Content-Type': 'text/plain; charset=utf-8',
      'Content-Length': str(len(data))
   },
   '__ow_path' : '/echo',
   '__ow_body' : b64encode(data)
}

put = {
   '__ow_method' : 'PUT',
   '__ow_headers' : {
      'Content-Type': 'text/plain',
      'Content-Length': str(len(data))
   },
   '__ow_path' : '/echo',
   '__ow_body' : b64encode(data)
}

index = dict(get)
index['__ow_path'] = '/'

def dump_response(response):
   print(response)

dump_response(invoke(app,index))

dump_response(invoke(app,get))

dump_response(invoke(app,post))

dump_response(invoke(app,put))
