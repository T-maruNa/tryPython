# -*- coding: utf-8 -*-
# 最小を計算
def minMove():
    minList = []
    maxCnt = 0
    for ant in antList:
        if(ant - (lineSize / 2) > 0):
            minList.append("右")
            outPoint = lineSize - ant
        else:
            minList.append("左")
            outPoint = ant

        if(outPoint > maxCnt):
            maxCnt = outPoint

    print('%d(%s)' % (maxCnt , ','.join(minList)))


# ---Main処理---
lineSize = 10
antList = [2,6,7]

# 位置の昇順にソート
antList.sort()
minMove()
