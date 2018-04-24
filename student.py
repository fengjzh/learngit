#!/bin/python36
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        return '%s:%s' % (self.__name,self.__score)
Lucy=Student("lucy li",98)
a=Lucy.print_score()
print(a)
#branch1
