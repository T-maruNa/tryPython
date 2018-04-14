# -*- coding: utf-8 -*-
import Ant

antList = []
positionList = [2,6,7]

# 位置の昇順にソート
positionList.sort()

for p in positionList:
    antList.append(Ant.Ant(p))

for ant in antList:
    ant.show()
