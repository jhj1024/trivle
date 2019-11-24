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

    sql = "INSERT INTO RECENT VALUE('" + destination + "');"

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
    cursor.execute(tsql) #쿼리 수행
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
def Listen_DTN_YES(parameters): #location table에서 DestinationForListen이 존재하는지 확인
    print('parameters')
    print(parameters)
    
    # parameters에서 필요한 인자 추출
    Destination = parameters['DestinationForListen']['value']  # 여행지
    print('Destination: ', Destination)
    
    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = "SELECT EXISTS (SELECT * FROM location WHERE place = '" + Destination + "');"
    print(sql)
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)
    print(rows[0])
    
    if(rows[0] == 1):
        hello = {'is_exist': 'exist'}
        recently(Destination)
        
    else:
        hello = {'is_exist': 'not_exist'}
    
    return hello
    
# ------------------------------------------------------------------------------
def Listen_DTN_NO(parameters): #recent table에서 Destination이 존재하는지 확인
    print('parameters')
    print(parameters)
    
    # query 결과물 받아서 return
    cursor = conn.cursor()
    sql = 'SELECT COUNT(R) FROM RECENT;'
    cursor.execute(sql)  # 쿼리 수행
    rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)
    print(rows)
    
    if(rows[0] != 0):
        hello = {'exist_recent': 'exist'}
        
    else:
        hello = {'exist_recent': 'not_exist'}
    
    return hello
# ------------------------------------------------------------------------------
def Listen(parameters): #해당 여행지와 해당 카테고리 들려줌 
    #여행지 있음 : CategoryForListen1 - list1
    #여행지 없음 : CategoryForListen2 - list3    
    print('parameters')
    print(parameters)
    
    is_exist = False #목적지 존재 여부
    cursor = conn.cursor()
    
    #목적지 존재
    if(parameters['DestinationForListen']['value']):
        Destination = parameters['DestinationForListen']['value'] #여행지
        CategoryForListen = parameters['CategoryForListen1']['value']  # 카테고리
        recently(Destination) #최근 목록 업데이트
        is_exist = True
        
    #목적지 없음
    else: #recent 테이블에서 최근 여행지 가져옴
        sql = 'SELECT R FROM RECENT;'
        cursor.execute(sql)  # 쿼리 수행
        rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)        
        Destination = rows[0]  #여행지
        CategoryForListen = parameters['CategoryForListen2']['value']  # 카테고리  
    
    # 카테고리에 따라 mysql에 저장한 attribute 이름으로 변환
    if (CategoryForListen == '개인'):
        Category = 'P'
        Category_check = 'P_checked'
    elif (CategoryForListen == '의류'):
        Category = 'C'
        Category_check = 'C_checked'
    elif (CategoryForListen == '생필품'):
        Category = 'S'
        Category_check = 'S_checked'
    elif (CategoryForListen == '전자기기'):
        Category = 'E'
        Category_check = 'E_checked'
    else:
        Category = 'G'
        Category_check = 'G_checked'
        
    print(Destination, Category)

    # query 결과물 받아서 return    
    sql = 'SELECT ' + Category + ' FROM ' + Destination + ' WHERE ' + Category_check + ' IS NULL LIMIT 5;'
    print(sql)
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
    
    if(is_exist == True):
        hello = {'list1': lists}
    
    else:
        hello = {'list3': lists}
    
    return hello

# ------------------------------------------------------------------------------
def Listen_Continue(parameters):
    #여행지 있음 : list2
    #여행지 없음 : list4
    print('parameters')
    print(parameters)
    
    is_exist = False #목적지 존재 여부
    cursor = conn.cursor()
    
    #목적지 존재
    if(parameters['DestinationForListen']['value']):
        Destination = parameters['DestinationForListen']['value'] #여행지
        CategoryForListen = parameters['CategoryForListen1']['value']  # 카테고리
        recently(Destination) #최근 목록 업데이트
        is_exist = True
        
    #목적지 없음
    else: #recent 테이블에서 최근 여행지 가져옴
        sql = 'SELECT R FROM RECENT;'
        cursor.execute(sql)  # 쿼리 수행
        rows = cursor.fetchone()  # 결과 가져옴(데이터타입: 튜플)        
        Destination = rows[0]  #여행지
        CategoryForListen = parameters['CategoryForListen2']['value']  # 카테고리  
    
    # 카테고리에 따라 mysql에 저장한 attribute 이름으로 변환
    if (CategoryForListen == '개인'):
        Category = 'P'
        Category_check = 'P_checked'
    elif (CategoryForListen == '의류'):
        Category = 'C'
        Category_check = 'C_checked'
    elif (CategoryForListen == '생필품'):
        Category = 'S'
        Category_check = 'S_checked'
    elif (CategoryForListen == '전자기기'):
        Category = 'E'
        Category_check = 'E_checked'
    else:
        Category = 'G'
        Category_check = 'G_checked'
        
    print(Destination, Category)

    # query 결과물 받아서 return
    sql ='SELECT '+Category+' FROM (SELECT @rownum:=@rownum+1 AS rnum, '+Category+', '+Category_check+' FROM '+Destination+' WHERE (@rownum:=0)=0) AS A WHERE '+Category_check+' IS NULL;'    
    print(sql)
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
    
    if(is_exist == True):
        hello = {'list2': lists}
    
    else:
        hello = {'list4': lists}
    
    return hello

# ------------------------------------------------------------------------------
def Checked_List(parameters):
    cur = conn.cursor()


    print(parameters['Destination']['value'])
    print("destination")
    if(parameters['Destination']['value']): #목적지가 있을 때
        sql = "SELECT * from location;"
        cur.execute(sql) #쿼리 수행
        rows = cur.fetchall() #결과 가져옴(데이터타입: 튜플)
        print(rows)

        #목적지가 location에 존재하면
        for i in rows:
            for j in i:
                if(j == parameters['Destination']['value']):
                   Destination = parameters['Destination']['value']
                   sql = "update " + Destination + " set " + parameters['item']['type'] + "_checked = 'C' where " + parameters['item']['type'] + " = '" + parameters['item']['value'] + "';"
                   print(sql)
                   cur.execute(sql)
                   conn.commit()
                   hello = {'check_recently':'yes'}
                   recently(Destination)
                   return hello

        #존재하지 않는 목적지일 경우
        hello = {'check_recently':'no'}
        return hello
    
    #사용자가 목적지를 말하지 않았을 때
    else:
        rsql = "SELECT * FROM RECENT;"
        cur.execute(rsql)  # 쿼리 수행
        rows = cur.fetchall()  # 결과 가져옴(데이터타입: 튜플)
        #최근 목적지가 존재하지 않을 때
        if (len(rows) == 0):
            hello = {'check_recently':'rno'}
            return hello
        #최근 목적지가 존재할 때
        else:
            Destination = str(rows)
            sql = "update " + Destination + " set " + parameters['item']['type'] + "_checked = 'C' where " + parameters['item']['type'] + "= '" + parameters['item']['value'] + "';"
            cur.execute(sql)
            conn.commit()
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
