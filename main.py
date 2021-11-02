# This is a sample Python script.

import load_data
import birthday_timeStamp
import itertools

class WhatIsYourName():
    def __init__(self,surname:str,birth_day:str,Expectation:str):
        self.surname= surname
        self.birth_day = birth_day
        self.Expectation = Expectation

        self.DBSession = load_data.get_conn(load_data.STR_PATH_SQLITE, True)
        self.name_list = []

    def get_my_name(self):

        bt = birthday_timeStamp.birthday_timeStamp(str_birthday_time=self.birth_day)
        bt_index_array = bt.get_birthday_time_random_id()
        #根据生日 随机生成的字序号 做笛卡尔积
        name_bt_index_array = [x for x in itertools.product(bt_index_array, bt_index_array)]
        surname_index = load_data.get_word_id(self.DBSession,self.surname)
        name_result_bt_index_array = [[surname_index,x[0],x[1]] for x in name_bt_index_array]
        return name_result_bt_index_array


    def print_hi(self,prefix,name_index_array):
        # 以三个字为例


        print(f'Hi, {prefix}\n')

        name = self.surname + \
        load_data.get_word_info(self.DBSession,name_index_array[1],"Word")+ \
        load_data.get_word_info(self.DBSession,name_index_array[2],"Word")

        self.name_list.append([self.surname,name,name_index_array])

        print(name+"\n")



if __name__ == '__main__':
    baby_name = WhatIsYourName(surname = "王",birth_day="2022-02-28 23:40:10",Expectation="")
    print(baby_name.get_my_name())
    baby_name_array = baby_name.get_my_name()

    for name in baby_name_array:
        baby_name.print_hi('你的名字是：',name)

    print(baby_name.name_list)


