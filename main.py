#coding:utf-8
import os
import json
import yaml
import glob
from flask import Flask, jsonify

app  = Flask(__name__)

@app.route('/', methods=["POST"])
def post_request():
    manifest = ManifestClass()
    service_names = manifest.serch_servicename()
    file_names = manifest.serch_filename(service_names)
    json_data = manifest.result_json(service_names, file_names)
    return json_data

@app.route('/<string:services>/<string:kinds>', methods=["GET"])
def yml_to_json (services, kinds):
    try:
        # filesの中身にあるサービス.ymlファイルをjson形式に変換する処理
        with open(f'files/{services}/{kinds}.yml') as file:
            yml = yaml.safe_load(file)
            js = json.dumps(yml, indent=2)
        return  js
    except FileNotFoundError:
        response = "error"
        return response
    
#filesフォルダにあるフォルダ名とファイル名をjson形式にして返却するやつ
class ManifestClass:
     # サービス名をlist形式で返す
    def serch_servicename(self):
        file_paths = []
        service_name = []

        paths = glob.glob("files/*")
        for path in paths:
            file_paths.append(glob.glob(f'{path}/*'))
        for file_path in file_paths:
            parts = file_path[0].split("/")
            service_name.append(parts[1])
        return service_name
    
    # サービス名からファイル名を取り出す
    def serch_filename(self, service_names):
        file_name = []
        for service_name in service_names:
            paths = glob.glob(f'files/{service_name}/*')
            service_files = []
            for path in paths:
                name = os.path.splitext(os.path.basename(path))[0]
                service_files.append(name)
            file_name.append(service_files)
        return file_name
    
    # サービス名とファイル名を結合させる処理
    def result_json(self, service_names, file_names):
        raw_data = {}
        for service_name, file_name in zip(service_names, file_names):
            print(service_name, file_name)
            raw_data[service_name] = file_name
        json_data = json.dumps(raw_data)
        return json_data
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
