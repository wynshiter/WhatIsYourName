


import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import word_dictionary

STR_PATH_SQLITE = r'sqlite:///D:/code/python/WhatIsYourName/data/zidian.db3?check_same_thread=False'

def get_conn(dbname, Echo=True):
    try:
        engine = create_engine(dbname, echo=Echo)
        DBSession = scoped_session(sessionmaker())
        #DBSession.remove()#scoped_session 本身是线程隔离的，这块不需要remove
        DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)

        return DBSession


    except:
        DBSession.rollback()
        raise
    # finally:
    #     DBSession.close()

def get_id_line(DBSession,id:int):
    #DBSession = get_conn(STR_PATH_SQLITE, True)

    table_and_column_name = word_dictionary.WordDictionary
    filter = (word_dictionary.WordDictionary.id == id)

    one_line = DBSession.query(table_and_column_name).filter(filter).all()
    return one_line

def get_word_info(DBSession,id:int,field:str):

    one_line = get_id_line(DBSession,id)
    return one_line[0].get_info(field)

def get_word_id(DBSession,word:str):

    table_and_column_name = word_dictionary.WordDictionary
    filter = (word_dictionary.WordDictionary.Word == word)

    one_line = DBSession.query(table_and_column_name).filter(filter).all()
    return one_line[0].id



if __name__ == '__main__':


    DBSession = get_conn(STR_PATH_SQLITE, True)

    table_and_column_name = word_dictionary.WordDictionary
    filter = (word_dictionary.WordDictionary.id == 100)

    one_line = DBSession.query(table_and_column_name).filter(filter).all()
    print(one_line)
    print(one_line[0].Word)
    print(type(one_line[0].Word))

    print(get_word_info(DBSession,100,"Content"))

    print(get_word_id(DBSession,"丧"))