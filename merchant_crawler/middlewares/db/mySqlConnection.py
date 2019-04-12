#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import pandas


class mySqlconnection(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='123.56.50.42',
            user='85ido',
            password='85ido%MYSQL&',
            db='6k_take_out_dev',
        )
        self.cursor = self.conn.cursor()
        sql = 'select * from tf_f_cookie'  # 查询表中的现有数据
        df = pandas.read_sql(sql, self.conn)
        for cookies in df["cookie_json"].get_values():
            with open('cookie', 'w') as f:
                f.write(f'{cookies}')

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
