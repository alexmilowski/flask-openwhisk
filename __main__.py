from flaskwsk.handle import invoke
from web import app

def main(args):
   return invoke(app,args)
