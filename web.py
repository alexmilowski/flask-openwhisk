from flask import Flask,request,jsonify
from werkzeug.http import parse_options_header

app = Flask(__name__)

class Config(object):
   DEBUG=True

@app.route('/')
def index():
   return 'Hello!'

@app.route('/echo',methods=['GET','HEAD','POST','PUT','DELETE','OPTIONS'])
def echo():
   obj = {
     'method' : request.method,
     'headers' : dict(request.headers)
   }
   if request.method=='POST' or request.method=='PUT':
      contentType = parse_options_header(request.headers.get('Content-Type','application/octet-stream'))
      encoding = contentType[1].get('charset','utf-8')
      obj['data'] = request.data.decode(encoding)
   return jsonify(obj)

if __name__ == '__main__':
   app.config.from_object('web.Config')
   app.run()
