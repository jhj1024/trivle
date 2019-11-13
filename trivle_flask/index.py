# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:27:54 2019

@author: JUNG
"""

import pymysql
conn = pymysql.connect(host='223.194.46.68', user='guest', password='1q2w3e4r!', db='my_db', charset='utf8mb4')

'''
with conn.cursor() as cursor:
    sql = 'SELECT * FROM my_db.adtext'
    cursor.execute(sql)
    temp1 = cursor.fetchall()
'''
def listen_list(parameters):
    print('parameters')
    print(parameters)
    hello = {'destination':'hello'}
    return hello