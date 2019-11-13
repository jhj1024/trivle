# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:44:32 2019

@author: JUNG
"""

from flask import Flask, jsonify
from flask import request
import json
import index

app = Flask(__name__)


def actionRequest(action):
    print('action')
    print(action)
    actionName = action['actionName'] #actionName 추출
    parameters = action['parameters'] #parameters 추출
    
    #python은 switch문이 없으므로 if-else문으로 대체
    if(actionName == 'Set_List'):
        output = index.listen_list(actionName, parameters)
        
    elif(actionName == 'Delete_List'):
        output = index.listen_list(actionName, parameters)
        
    elif(actionName == 'Listen_List'):
        output = index.listen_list(actionName, parameters)
        
    elif(actionName == 'Listen_Tip'):
        output = index.listen_list(actionName, parameters)
    else:
        output = {}
           
    return output

def NPKResponse(output):
    npkResponse = {'version':'2.0', 'resultCode':'OK', 'output':output, 'directives': []}
    print('npkResponse')
    print(npkResponse)
    return npkResponse

@app.route("/nugu", methods=['POST'])
def nugu():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    print('body')
    print(body)
    
    action = body['action'] #action부분만 추출
    output = actionRequest(action) #actionRequest함수 호출
    print('output')
    print(output)
    npkResponse = NPKResponse(output)
    return jsonify(npkResponse)

if __name__ == '__main__':    
    app.run(host="127.0.0.1", port=3000)