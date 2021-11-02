#!/usr/bin/python
# 20823 个汉字的话，我们使用 随机生成这些汉字 的id 范围
#-*-coding:utf-8-*-
import time, datetime
import random;


class birthday_timeStamp():
    def __init__(self,str_birthday_time="2022-02-28 23:40:00"):
        self.HanZi_Total_Number = 20823
        self.Beixuan_Number = 6

        self.str_birthday_time = str_birthday_time
        self.timeArray = time.strptime(str_birthday_time, "%Y-%m-%d %H:%M:%S")
        self.timeStamp = int(time.mktime(self.timeArray))
        self.randomNumArray = []

    def get_birthday_time_random_id(self):

        random.seed(self.timeStamp)
        for i in range (0,self.Beixuan_Number):
            randomNum=random.randint(0,self.HanZi_Total_Number);
            self.randomNumArray.append(randomNum)


        return self.randomNumArray