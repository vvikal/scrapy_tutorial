# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class TutorialPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
        'localhost',
        27017
        )
        db= self.conn['myquotes']
        self.collection = db['quotes_tb']
    def process_item(self,item,spider):
        self.collection.insert(dict(item))
        return item



# import mysql.connector
#
#
# class TutorialPipeline(object):
#     def __init__(self):
#         self.set_connection()
#         self.table_tb()
#
#     def set_connection(self):
#         self.conn =mysql.connector.connect(
#             host='localhost',
#             user='root',
#             passwd='root',
#             database='myquotes'
#         )
#         self.curr=self.conn.cursor( )
#     def table_tb(self):
#         self.curr.execute("""drop table if exists quotes""")
#         self.curr.execute("""create table quotes(
#                         title text,
#                         author text,
#                         tags text
#                         )""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item
#
#     def store_db(self,item):
#
#         self.curr.execute("""insert into quotes values(%s,%s,%s)""",(
#                         item['title'][0],
#                         item['Author'][0],
#                         item['tags'][0]
#                         ))
#         self.conn.commit()
