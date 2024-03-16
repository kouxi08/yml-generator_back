#coding:utf-8

from flask import Flask, render_template

app  = Flask(__name__)

@app.route("/test")
def index():
    return "Hello World"

@app.route('/<string:kinds>', methods=["GET"])
def yml_to_json (kinds):

    return  kinds
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
