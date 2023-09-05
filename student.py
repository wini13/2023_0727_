class Student:
    def __init__(self,name:str,chinese:int,math:int,english:int):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    #實體方法method
    def total(self)->int:
        return self.chinese + self.math + self.english
    
    #建立property->類似method,沒有參數,一定傳出一個值
    @property
    def average(self)->float:
        return round(self.total()/3.0,2)
    
    def __repr__(self):
        return f'我是學生實體，我的名字是{self.name}'

import random
def getStudent(n:str)->Student:
    ch=random.randint(50,101)
    en=random.randint(50,101)
    math=random.randint(50,101)
    return Student(name=n,chinese=ch,math=math,english=en)