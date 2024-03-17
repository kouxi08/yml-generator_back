#coding:utf-8
import os
import json
import yaml
import glob
from flask import Flask, jsonify

app  = Flask(__name__)

@app.route("/test")
def index():
    return "Hello World"

@app.route('/', methods=["POST"])
def post_request():
    manifest = ManifestClass()
    service_names = manifest.serch_servicename()
    file_names = manifest.serch_filename(service_names)
    return file_names

@app.route('/<string:services>/<string:kinds>', methods=["GET"])
def yml_to_json (services, kinds):
    # filesの中身にあるサービスのymlファイルをjson形式に変換する処理
    with open(f'files/{services}/{kinds}.yml') as file:
        yml = yaml.safe_load(file)
        js = json.dumps(yml, indent=2)
    return  js

class ManifestClass:
    # servie名からファイル名を取り出す
    def serch_filename(self, services_name):
        file_name = []
        for service_name in services_name:
            paths = glob.glob(f'files/{service_name}/*')
            for path in paths:
                name = os.path.splitext(os.path.basename(path))[0]
                file_name.append(name)
        return file_name
    
    # service名をlist形式で返す
    def serch_servicename(self):
        file_paths = []
        service_name = []

        paths = glob.glob("files/*")
        for path in paths:
            file_paths.append(glob.glob(f'{path}/*'))
        for file_path in file_paths:
            service_paths = file_path[0]
            parts = service_paths.split("/")
            service_name.append(parts[1])
        return service_name
    def result_json():
        # jsonify({'file_paths': file_paths})
        return
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
