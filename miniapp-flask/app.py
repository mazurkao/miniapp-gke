# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request
import json
import logging.config
import yaml

# ログ設定ファイルからログ設定を読み込む。★
logging.config.dictConfig(yaml.load(open('logging.yaml').read(), Loader=yaml.SafeLoader))
# logging.config.fileConfig('logging.conf')
 
# ログ設定ファイルからログ設定を読み込み
logger = logging.getLogger()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    logger.debug('"Hello World!"を出力') 
    return "Hello World!"

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    logger.debug('"Yes, it is ~!"を出力') 
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

if __name__ == "__main__":
    logger.debug('port=5555へ接続') 
    app.run(host='0.0.0.0',port=5555,debug=True)
