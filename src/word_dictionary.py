# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: word_dictionary.py
@time: 2021/1/7 10:34
@desc:
'''

import sys
import os
from sqlalchemy import Column, TEXT, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import scoped_session, sessionmaker

# CURRENT_URL = os.path.dirname(__file__)
# PARENT_URL = os.path.abspath(os.path.join(CURRENT_URL, os.pardir))
# sys.path.append(PARENT_URL)

COLUMN_NAME = ['id',
                   'word',
                   'pinyin_1',
                   'pinyin_2',
                   'wubi',
                   'bushou',
                   'bihua',
                   'content',
                   'remark'
                   ]


Base = declarative_base()


class WordDictionary(Base):
    '''
    # 定义汉字对象:

    '''
    __tablename__ = 'WordDictionary'

    # 表的结构:

    id = Column(Integer, primary_key=True, unique=True)
    Word = Column(String, nullable=False, unique=True)
    PinYin_1 = Column(String)
    PinYin_2 = Column(String)
    WuBi = Column(String)
    BuShou = Column(String)
    BiHua = Column(Integer)
    Content = Column(String)
    Remark = Column(String)

    def get_info(self,info_column_name):
        return str(getattr(self, info_column_name))

    def __repr__(self):
        return "<id(id ='%s' ," \
               " word = '%s', " \
               "PinYin_1 = '%s', " \
               "PinYin_2 = '%s', " \
               "WuBi = '%s', " \
               "BuShou = '%s', " \
               "BiHua = '%s', " \
               "Content = '%s', " \
               "Remark = '%s'>" % (
                   self.id,
                   self.Word,
                   self.PinYin_1,
                   self.PinYin_2,
                   self.WuBi,
                   self.BuShou,
                   self.BiHua,
                   self.Content,
                   self.Remark

               )
