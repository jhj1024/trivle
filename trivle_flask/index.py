# -*- coding: utf-8 -*-
"""
trivle 함수 선언부
"""
from random import *
import pymysql
import json
import re


# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle', use_unicode=True, charset='utf8')

# ------------------------------------------------------------------------------
def Set_Location(parameters):
    print('Set_List: parameters')
    print('Set:' + parameters['DestinationForSet']['value'])


    cur = conn.cursor()
    sql = 'SELECT * from location;'
    cur.execute(sql) #쿼리 수행
    rows = cur.fetchall() #결과 가져옴(데이터타입: 튜플)
    print(rows)

    for i in rows:
        for j in i:
            if(j == parameters['DestinationForSet']['value']):
                hello = {'Destination1':'존재'}#하는 리스트예요. 듣기를 원하시면 ' + parameters['DestinationForSet']['value'] + ' 리스트 들려줘라고 말씀해주세요'}
                return hello


    #존재하는 리스트 return

#------------------------------------------------------------------------------
def Set_List(parameters):
    #여행지 + 일수 -> 리스트 생성
    cur = conn.cursor()

    
    if(parameters['DestinationForSet']['type'] == 'HEY'):
        if(int(parameters['FewDay']['value'])<=7):

            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM OS;"
            cur.execute(setsql)
            print('out create table')
        else:
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM OL;"
            cur.execute(setsql)
            print('out long create table')

    else:
        if(int(parameters['FewDay']['value'])<=7):
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM IS;"
            cur.execute(setsql)
            print('in create table')
        else:
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM IL;"
            cur.execute(setsql)
            print('in long create table')

    cur = conn.cursor()
    plusql = "Insert into location(L, fewday) value('" + parameters['DestinationForSet']['value'] + "', '" + parameters['FewDay']['value'] + "');" 
    print(11111111111111111111111111111)
    print(plusql)
    cur.execute(plusql)
    hello = {'parameter':parameters['DestinationForSet']['value']+' 여행 체크 리스트를 만들었어요'}
    return hello


# ------------------------------------------------------------------------------
def Delete_List(parameters):
    print('parameters')
    print(parameters)

    Destination = parameters['DestinationForDelete']['value']  # 여행지

    #print(Destination)
    # query 결과물 받아서 return
    cursor = conn.cursor()
    check = "SHOW TABLES LIKE '" + Destination + "';"
    cursor.execute(check)
    res = cursor.fetchall()
    if len(res) == 0:
        result = '존재하지 않는 여행지에요.'
    else:
        sql = 'DROP TABLE ' + Destination + ';'
        cursor.execute(sql)  # 쿼리 수행
        result = Destination + ' 여행 리스트를 삭제할게요.'

    print('@@')
    print(result)
    hello = {'DONE': result}
    return hello

# ------------------------------------------------------------------------------
def Listen_Location(parameters):
    print('parameters')
    print(parameters)

    # parameters에서 필요한 인자 추출
    Destination = parameters['DestinationForListen']['value']  # 여행지
    print('Destination: ', Destination)
    
    Destination = str(Destination)
    Destination = re.sub('[,())\'\"]', '',Destination)
    
    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = 'SELECT EXISTS (SELECT * FROM location WHERE L=%s);'
    cursor.execute(sql, Destination)  # 쿼리 수행
    rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)
    print(rows)
    
    #if(rows[0] == '0'):
        
    

def Listen_List(parameters):
    print('parameters')
    print(parameters)

    # parameters에서 필요한 인자 추출
    Destination = parameters['DestinationForListen']['value']  # 여행지
    Category = parameters['CategoryForListen']['value']  # 카테고리
    print(Destination, Category)

    # 카테고리에 따라 mysql에 저장한 attribute 이름으로 변환
    if (Category == '개인'):
        attribute = 'P'
    elif (Category == '의류'):
        attribute = 'C'
    elif (Category == '생필품'):
        attribute = 'S'
    elif (Category == '전자기기'):
        attribute = 'E'
    else:
        attribute = 'G'

    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = 'SELECT ' + attribute + ' FROM ' + Destination + ';'
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchall()  # 결과 가져옴(데이터타입: 튜플)
    print(rows)

    lists = []
    for elem in rows:
        if (elem[0] != ''):
            element = str(elem)
            element = re.sub('[,()\'\"]', '',element)
            lists.append(element)
            
    print(lists)
    
    lists = str(lists)
    lists = re.sub('[()\[\]\'\"]', '',lists)
    hello = {'list': lists}
    
    return hello
# ------------------------------------------------------------------------------
def Listen_Tip():
    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = "SELECT * from T"
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchall()

    rand = randint(0, len(rows)-1)
    print(rows[rand])
    result = rows[rand]
    result = result
    #lists = [list(elem) for elem in rows]  # 튜플을 리스트로 변환

    hello = {'TIP':result}
    return hello
# ------------------------------------------------------------------------------
