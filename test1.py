from flask import Flask
from flask import request

app = Flask(__name__ )

@app.route("/")
def test1():
    return "<h1> This is my first python rest </h1>"

@app.route("/test2")
def test2():
    a=2+3
    return "what are you doing today {}".format(a)

@app.route("/test3")
def test3():
    
    return "i am returning the same value {}".format(request.args.get('x'))

if __name__=="__main__":
    app.run(host="0.0.0.0")