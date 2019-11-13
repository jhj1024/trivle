# -*- coding: utf-8 -*-
"""
trivle 서버 (python run.py)
"""
from flask import Flask, jsonify
from flask import request
import index
app = Flask(__name__)

#------------------------------------------------------------------------------
def NPKRequest(body):
    print('body')
    print(body)
    
    action = body['action'] #action부분만 추출
    output = actionRequest(action) #actionRequest함수 호출
    
    print('output')
    print(output)
    
    npkResponse = NPKResponse(output)
    return npkResponse
#------------------------------------------------------------------------------    
def actionRequest(action):
    print('action')
    print(action)
    actionName = action['actionName'] #actionName 추출
    parameters = action['parameters'] #parameters 추출
    
    #python은 switch문이 없으므로 if-else문으로 대체
    if(actionName == 'Set_List'):
        output = index.Set_List(parameters)
        
    elif(actionName == 'Delete_List'):
        output = index.Delete_List(parameters)
        
    elif(actionName == 'Listen_List'):
        output = index.Listen_List(parameters)
        
    elif(actionName == 'Listen_Tip'):
        output = index.Listen_Tip(parameters)
    else:
        output = {}
           
    return output
#------------------------------------------------------------------------------
def NPKResponse(output):
    npkResponse = {'version':'2.0', 'resultCode':'OK', 'output':output, 'directives': []}
    print('npkResponse')
    print(npkResponse)
    return npkResponse
#------------------------------------------------------------------------------

@app.route("/nugu/Set_List", methods=['POST'])
def nugu_set():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return jsonify(npkResponse)

@app.route("/nugu/Delete_List", methods=['POST'])
def nugu_delete():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return jsonify(npkResponse)

@app.route("/nugu/Listen_List", methods=['POST'])
def nugu_listen():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return jsonify(npkResponse)

@app.route("/nugu/Listen_Tip", methods=['POST'])
def nugu_tip():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return jsonify(npkResponse)

if __name__ == '__main__':    
    app.run(host="0.0.0.0", port=3000)