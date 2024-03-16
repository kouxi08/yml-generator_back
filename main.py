#coding:utf-8
import os
import json
import yaml
# import yaml
from flask import Flask, render_template

app  = Flask(__name__)

@app.route("/test")
def index():
    return "Hello World"

@app.route('/<string:services>/<string:kinds>', methods=["GET"])
def yml_to_json (services, kinds):
    with open(f'files/{services}/{kinds}.yml') as file:
        yml = yaml.safe_load(file)
        js = json.dumps(yml, indent=2)
    return  js
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
