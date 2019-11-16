# -*- coding: utf-8 -*-
"""
trivle 함수 선언부
"""
from random import *
import pymysql

# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle',
                       charset='utf8mb4')

# ------------------------------------------------------------------------------
def Set_List(parameters):
    print('Set_List: parameters')
    print('Set:' + parameters['DestinationForSet']['value'])

    cur = conn.cursor()
    sql = 'SELECT * from location;'
    cur.execute(sql) #쿼리 수행
    rows = cur.fetchall() #결과 가져옴(데이터타입: 튜플)
    print(rows)
    
    exist = 0

    hello = {'Destination1':'춘천 여행 리스트 생성과 같이 말씀해주세요'}

    for i in rows:
        print(i)
        for j in i:
            print(j)
            if(j == parameters['DestinationForSet']['value']):
                hello = {'Destination1':'존재하는 리스트예요. 듣기를 원하시면 ' + parameters['DestinationForSet']['value'] + ' 리스트 들려줘라고 말씀해주세요'}
                return hello

    cur = conn.cursor()
    print(333333333333333333333333333333)
    print(parameters['FewDay']['value'])
    if(parameters['DestinationForSet']['type'] == 'HEY'):
        if(int(parameters['FewDay']['value'])<=7):
            print(11111111111111111111111)
            setsql = "CREATE TABLE ' +  parameters['DestinationForSet']['value'] + ' SELECT * FROM OS;"
            print(222222222222222222222222)
            cur.execute(setsql)
            print('out create table')
        else:
            setsql = 'CREATE TABLE ' +  parameters['DestinationForSet']['value'] + ' SELECT * FROM OL;'
            cur.execute(setsql)
            print('out long create table')
    
    else:
        if(int(parameters['FewDay']['value'])<=7):
            setsql = 'CREATE TABLE ' +  parameters['DestinationForSet']['value'] + ' SELECT * FROM IS;'
            cur.execute(setsql)
            print('in create table')
        else:
            setsql = 'CREATE TABLE ' +  parameters['DestinationForSet']['value'] + ' SELECT * FROM OL;'
            cur.execute(setsql)
            print('in long create table')

    hello = {'parameter':parameters['DestinationForSet']['value']+' 여행 체크 리스트를 만들었어요'}
    return hello



# ------------------------------------------------------------------------------
def Delete_List(parameters):
    print('parameters')
    print(parameters)

    Destination = parameters['DestinationForDelete']['value']  # 여행지

    print(Destination)
    # query 결과물 받아서 return
    cursor = conn.cursor()
    check = "SHOW TABLES LIKE '" + Destination + "';"
    cursor.execute(check)
    result = cursor.fetchall()
    if len(result) == 0:
        print('테이블 존재 안 함')
    else:
        sql = 'DROP TABLE ' + Destination + ';'
        cursor.execute(sql)  # 쿼리 수행


# ------------------------------------------------------------------------------
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
            print(type(elem))
            element = elem
            lists.extend(list(element))
            
    print(lists)

    hello = {'list': lists}  # 'list'는 각자 action parameter와 일치시킬 것
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
    result = result.encode('utf-8')
    #lists = [list(elem) for elem in rows]  # 튜플을 리스트로 변환

    hello = {'TIP':result}
    return hello
# ------------------------------------------------------------------------------
