# -*- coding: utf-8 -*-
"""
trivle 함수 선언부
"""
from random import *
import pymysql
import json
import re

Destination = ''
attribute = ''

# mysql 접속
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle', use_unicode=True, charset='utf8')

def recently(destination):
    #쿼리문을 통해서 최근 여행지 update 하는 함수
    cur = conn.cursor()
    tsql = "Truncate table RECENT"
    cur.execute(tsql) #쿼리 수행
    conn.commit()

    sql = "Insert into location value('" + destination + "');"

    cur.execute(sql)
    conn.commit()


# ------------------------------------------------------------------------------
def Set_Location(parameters):

    print('Set_List: parameters')
    print('Set:' + parameters['DestinationForSet']['value'])

    recently(parameters['DestinationForSet']['value'])

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
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM trivle.OS;"
            cur.execute(setsql)
            print('out create table')
        else:
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM trivle.OL;"
            cur.execute(setsql)
            print('out long create table')

    else:
        if(int(parameters['FewDay']['value'])<=7):
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM trivle.IS;"
            cur.execute(setsql)
            print('in create table')
        else:
            setsql = "CREATE TABLE " + parameters['DestinationForSet']['value'] + " SELECT * FROM trivle.IL;"
            cur.execute(setsql)
            print('in long create table')
    
    conn.commit()
    plusql = "Insert into location value('" + parameters['DestinationForSet']['value'] + "', '" + parameters['FewDay']['value'] + "');" 
    print(123123123)
    print(plusql)
    cur.execute(plusql)
    conn.commit()
    hello = {'parameter':parameters['DestinationForSet']['value']+' 여행 체크 리스트를 만들었어요'}
    return hello


# ------------------------------------------------------------------------------
def Delete_List(parameters):
    print('parameters')
    print(parameters)

    Destination = parameters['DestinationForDelete']['value']  # 여행지

    cursor = conn.cursor()
    tsql = "Truncate table RECENT"
    cur.execute(tsql) #쿼리 수행
    conn.commit()

    #print(Destination)
    #query 결과물 받아서 return
    check = "SHOW TABLES LIKE '" + Destination + "';"
    cursor.execute(check)
    res = cursor.fetchall()
    if len(res) == 0:
        result = '존재하지 않는 여행지에요.'
    else:
        sql = 'DROP TABLE ' + Destination + ';'
        cursor.execute(sql)  # 쿼리 수행
        conn.commit()
        
        delsql = "Delete from trivle.location where place = '" + Destination + "';"
        print(1111111111111111111)
        print(delsql)
        cursor.execute(delsql)
        conn.commit()
        result = Destination + ' 여행 리스트를 삭제할게요.'

    print('@@')
    print(result)
    hello = {'DONE': result}
    return hello

# ------------------------------------------------------------------------------
'''
def Listen_Location(parameters):
    print('parameters')
    print(parameters)

    # parameters에서 필요한 인자 추출
    Destination = parameters['Destination']['value']  # 여행지
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
'''        
    
# ------------------------------------------------------------------------------
def Listen_List(parameters):
    print('parameters')
    print(parameters)

    if(parameters['DestinationForListen']['value']) #목적지가 존재하면 최근 목록 업데이트
        recently(parameters['DestinationForSet']['value'])

    # parameters에서 필요한 인자 추출
    DestinationForListen = parameters['DestinationForListen']['value']  # 여행지
    Destination = DestinationForListen
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
    sql = 'SELECT ' + attribute + ' FROM ' + Destination + ' LIMIT 5;'
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
    hello = {'lists': lists}
    
    return hello

# ------------------------------------------------------------------------------
def Listen(parameters):
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
    sql = 'SELECT ' + attribute + ' FROM ' + Destination + ' LIMIT 5;'
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
    hello = {'lists': lists}
    
    return hello
# ------------------------------------------------------------------------------
def Checked_List(parameters):
    cursor = conn.cursor()


    if(parameters['Destination']['value']): #목적지가 있을 때
        sql = 'SELECT * from location;'
        cur.execute(sql) #쿼리 수행
        rows = cur.fetchall() #결과 가져옴(데이터타입: 튜플)
        print(rows)

        #목적지가 location에 존재하면
        for i in rows:
            for j in i:
                if(j == parameters['DestinationForSet']['value']):
                   Destination = parameters['Destination']['value']
                   sql = "update " + Destination + " set " + parameters['itme']['type'] + "_checked = 'C' where " + parameters['item']['type'] + "= " + parameters['item']['value'] + "';"
                   cursor.exxectue(sql)
                   hello = {'check_recently':'yes'}
                   return hello

        #존재하지 않는 목적지일 경우
        hello = {'check_recently':'no'}
        return hello
    
    #사용자가 목적지를 말하지 않았을 때
    else:
        rsql = "SELECT * FROM RECENT;"
        cursor.execute(sql)  # 쿼리 수행
        rows = cursor.fetchall()  # 결과 가져옴(데이터타입: 튜플)
        #최근 목적지가 존재하지 않을 때
        if (len(rows) == 0):
            hello = {'check_recently':'rno'}
            return hello
        #최근 목적지가 존재할 때
        else:
            Destination = str(rosw)
            sql = "update " + Destination + " set " + parameters['itme']['type'] + "_checked = 'C' where " + parameters['item']['type'] + "= " + parameters['item']['value'] + "';"
            cursor.exxectue(sql)
            hello = {'check_recently': 'yes'}
            return hello

    return hello

#--------------------------------------------------------------------------------- 
def Listen_Tip():
    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = "SELECT * from T"
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchall()

    rand = randint(0, len(rows)-1)
    print(rows[rand])
    result = rows[rand]
    #lists = [list(elem) for elem in rows]  # 튜플을 리스트로 변환
    result = str(result)
    hello = {'TIP':result}
    return hello
# ------------------------------------------------------------------------------
