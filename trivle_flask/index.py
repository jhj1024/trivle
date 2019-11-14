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
    print('parameters')
    print(parameters)

    hello = {'parameter': 'hello'}
    return hello


# ------------------------------------------------------------------------------
def Delete_List(parameters):
    print('parameters')
    print(parameters)

    hello = {'parameter': 'hello'}
    return hello


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
        if (elem != ''):
            lists.extend(list(elem))
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
    lists = [list(elem) for elem in rows]  # 튜플을 리스트로 변환

    hello = {'TIP':rows[rand]}
    return hello
# ------------------------------------------------------------------------------
