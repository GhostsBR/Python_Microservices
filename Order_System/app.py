import requests
import os
import json
import pandas as pd
from flask import Flask, request
from Controller import ApiController

from Controller import InputController
ic = InputController.InputControl()

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
ac = ApiController.ApiControl()

@app.route('/api/v1/orders', methods=['GET'])
def users_route():
    try:
            req = request.data.decode("utf-8")
            req = json.loads(req)
            req = dict(req)
    except:
        return 'Error: Cannot convert data into json!', 400
    if not ic.verify_auth(req): return "Error: Authentication failed!", 401
    try:
        req['id']
    except:
        req['id'] = "none"
    if not req['id'] == "none":
        result = ac.order_list_by_user(req)
        return result.content, result.code
    else:
        result = ac.order_list()
        return result.content, result.code

@app.route('/api/v1/order', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_route():
    if request.method == 'GET':
        try:
            req = request.data.decode("utf-8")
            req = json.loads(req)
            req = dict(req)
        except:
            return 'Error: Cannot convert data into json!', 400
        if not ic.verify_auth(req): return "Error: Authentication failed!", 401
        result = ac.order_show(req)
        return result.content, result.code
    elif request.method == 'POST':
        try:
            req = request.data.decode("utf-8")
            req = json.loads(req)
            req = dict(req)
        except:
            return 'Error: Cannot convert data into json!', 400
        if not ic.verify_auth(req): return "Error: Authentication failed!", 401
        result = ac.order_create(req)
        return result.content, result.code
    elif request.method == 'PUT':
        try:
            req = request.data.decode("utf-8")
            req = json.loads(req)
            req = dict(req)
        except:
            return 'Error: Cannot convert data into json!', 400
        if not ic.verify_auth(req): return "Error: Authentication failed!", 401
        result = ac.order_update(req)
        return result.content, result.code
    elif request.method == 'DELETE':
        try:
            req = request.data.decode("utf-8")
            req = json.loads(req)
            req = dict(req)
        except:
            return 'Error: Cannot convert data into json!', 400
        if not ic.verify_auth(req): return "Error: Authentication failed!", 401
        result = ac.order_remove(req)
        return result.content, result.code


if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('DOMAIN'), port=os.getenv('PORT'))
