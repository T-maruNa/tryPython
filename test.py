# -*- coding: utf-8 -*-

# 引数が偶数か奇数か判断するメソッド
def checkEven(i):
    if((i % 2) == 0):
        return True
    else:
        return False
max = 10
for i in range(max):
    if(checkEven(i)):
        print("偶数")
    else:
        print("奇数")
