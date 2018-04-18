# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# POJ No.1852
# 長さLcmの竿の上をn匹の蟻が毎秒1cm/sの速さで歩いています．
# 蟻が竿の端に達すると竿の下に直ちに落ちていきます．
# (竿の上は狭くてすれ違うことができないので)2匹の蟻が出会うと，
# それぞれ反対の方向を向いて歩き始めます．
# 各蟻iについて，初期位置(左端からの距離 xi)は分かりますが，
# 残念なことに，どちらの方向に向かって歩いているのかは分かりません．
# すべての蟻が竿から落ちるまでにかかる最小の時間と最大の時間をそれぞれ求めてください．
# -------------------------------------------------------------

import sys

# 入力値のチェック
def validCheck():
    errorFlg = False
    if(lineSize < len(antList)):
        print("蟻の数に対して、竿の長さが短すぎます")
        errorFlg = True
    if(filter(lambda ant:ant > lineSize or ant <= 0, antList)):
        print("すでに転落している蟻がいます")
        errorFlg = True

    if(errorFlg):
        sys.exit()

# 最小を計算
def minMove():
    minList = []
    maxCnt = 0
    for ant in antList:
        if(ant - midP > 0):
            minList.append("右")
            # 右端までの距離
            outPoint = lineSize - ant
        else:
            minList.append("左")
            # 左端までの距離
            outPoint = ant

        if(outPoint > maxCnt):
            maxCnt = outPoint

    print('%d(%s)' % (maxCnt , ','.join(minList)))

# 最大を取得
# --いろいろグダグダ考えたが、出会った方が時間がかかるパターンはない
# --最小を逆の計算で良い
def maxMove():
    # 左端,右端を取得
    first = 0
    last = len(antList) - 1
    maxL = lineSize - antList[first]
    maxR = antList[last]
    maxList = []

    if(maxL > maxR):
        maxCnt = maxL
        vector = "右"
    else:
        maxCnt = maxR
        vector = "左"

    for i in range(len(antList)):
        maxList.append(vector)

    print('%d(%s)' % (maxCnt , ','.join(maxList)))

# ---Main処理---
lineSize = 30
antList = [2,15,16,29]
midP = lineSize / 2

# 位置の昇順にソート
antList.sort()
validCheck()
minMove()
maxMove()
