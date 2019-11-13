# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:27:54 2019

@author: JUNG
"""

import pymysql
conn = pymysql.connect(host='45.119.146.152', port=1024, user='trivle', password='Trivle_96', db='trivle', charset='utf8mb4')


def Set_List(parameters):
    print('parameters')
    print(parameters)
    
    hello = {'parameter':'hello'}
    return hello

def Delete_List(parameters):
    print('parameters')
    print(parameters)
    
    hello = {'parameter':'hello'}
    return hello

def Listen_List(parameters):
    print('parameters')
    print(parameters)
    
    Destination = parameters['DestinationForListen']['value']
    Category = parameters['CategoryForListen']['value']
    print(Destination, Category)
    
    if(Category == '개인'):
        Category = 'P'
    elif(Category == '의류'):
        Category = 'C'
    elif(Category == '생필품'):
        Category = 'S'
    elif(Category == '전자기기'):
        Category = 'E'
    else:
        Category = 'G'
    
    cursor = conn.cursor()
    sql = 'SELECT ' + Category + ' FROM ' + Destination + ';'
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)
    lists = [list(elem) for elem in rows]
    
    hello = {'list':lists}
    return hello

def Listen_Tip(parameters):
    print('parameters')
    print(parameters)
    
    hello = {'parameter':'hello'}
    return hello
