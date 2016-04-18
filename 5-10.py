#! /urs/bin/env python
#encoding: utf-8

'''写一对函数来进行华氏度到摄氏度的转换。转换公式为C = (F - 32) * (5 / 9)
应该在这个练习中使用真正的除法， 否则你会得到不正确的结果'''


def caltem(F):
    C=(F-32)*(float(5)/9)
    return(C)
    
print(caltem(48))