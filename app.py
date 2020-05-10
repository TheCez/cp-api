from flask import Flask,render_template,request,redirect
import time
from flask import  jsonify,json
import codechef
import codeforces
from traceback import print_exc
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = 'thecez'
CORS(app)

@app.route('/')
def home():
    return 'Welcome to Unofficial Codechef API'

@app.route('/cc/present')
def result1():
    data=codechef.present()
    return str(data)

@app.route('/cc/future')
def result2():
    data=codechef.future()
    return str(data)

@app.route('/cc/past')
def result3():
    data=codechef.past()
    return str(data)

@app.route('/cf/present')
def result4():
    data=codeforces.present()
    return str(data)

@app.route('/cf/past')
def result5():
    data=codeforces.past()
    return str(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True,threaded = True)
