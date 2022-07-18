from flask import Flask
from flask_sock import Sock
import pkg_resources


app = Flask(__name__)
sock = Sock(app)
@sock.route('/reverse')

def reverse(ws):
   while True:
        text = ws.receive() 
        ws.send(text[::-1])
     #return pkg_resources.get_distribution('Flask').version
@sock.route('/version')      
def  version():
         print( flask --version)
