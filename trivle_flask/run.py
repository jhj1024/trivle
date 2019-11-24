#-*- coding: utf-8 -*-
"""
trivle 서버 (python run.py)
"""
from flask import Flask, make_response, Response
import json
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

    if(actionName == 'Set_Location'):
        output = index.Set_Location(parameters)

    elif(actionName == 'Set_List'):
        output = index.Set_List(parameters)
        
    elif(actionName == 'Delete_List'):
        output = index.Delete_List(parameters)
        
    elif(actionName == 'Listen_DTN_YES'):
        output = index.Listen_DTN_YES(parameters)
        
    elif(actionName == 'Listen_DTN_NO'):
        output = index.Listen_DTN_NO(parameters)
        
    elif((actionName == 'Listen_Category1') or (actionName == 'Listen_Category2')):
        output = index.Listen(parameters)
        
    elif((actionName == 'Listen_Continue1') or (actionName == 'Listen_Continue2')):
        output = index.Listen_Continue(parameters)
        
    elif(actionName == 'Checked_List'):
        output = index.Checked_List(parameters)
            
    elif(actionName == 'Listen_Tip'):
        output = index.Listen_Tip()
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
#------------------------------------------------------------------------------
@app.route("/nugu/Set_Location", methods=['POST'])
def nugu_set1():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Set_List", methods=['POST'])
def nugu_set():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Delete_List", methods=['POST'])
def nugu_delete():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_DTN_YES", methods=['POST'])
def nugu_listen1():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_DTN_NO", methods=['POST'])
def nugu_listen2():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_Category1", methods=['POST'])
def nugu_listen3():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_Category2", methods=['POST'])
def nugu_listen4():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_Continue1", methods=['POST'])
def nugu_listen5():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_Continue2", methods=['POST'])
def nugu_listen6():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Listen_Tip", methods=['POST'])
def nugu_tip():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)   
    return (json.dumps(npkResponse, ensure_ascii=False))

@app.route("/nugu/Checked_List", methods=['POST'])
def nugu_check():
    body = request.json #전송받은 json 객체를 dictionary로 변환 
    npkResponse = NPKRequest(body)   
    return (json.dumps(npkResponse, ensure_ascii=False))
#------------------------------------------------------------------------------
if __name__ == '__main__':    
    app.run(host="0.0.0.0", port=3000)