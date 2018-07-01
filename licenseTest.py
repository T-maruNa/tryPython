def separate():
    print('------------------------------------------------')


array = [1,2,3,]
array2 = {'one':1,'two':2,'fore':4}
for key, value in array2.items():
    print(key,value)

# output range(0,5)
print(range(5))
separate()

class ClassTest(object):
    """ クラス変数が共通(使いかた間違え) """
    list_in_class = []

    def add_list(self, v):
        # self.list = [] これがあれば共通化はされない
        self.list_in_class.append(v)

c1 = ClassTest()
c2 = ClassTest()

c1.add_list('c1')
c2.add_list('c2')

# c1のリストにc2もはいっている
for v in c1.list_in_class:
    print(v)

separate()

c = 3.0 + 5 , 2 * 5
print(c)

separate()

tp = 5,6,7,
#a,b,c,d = tp だとエラーになる
a,b,c = tp

print(tp)
#a,b,a = tp だと出力結果は7
print(a)

separate()
# {}でもいけるんやな
print('{} {}'.format('test','test2'))

separate()

# ループに入らなかったらelseに行く 意外とTrue Falseが大文字小文字判断する
while False:
    print('ループ内')
    break
else:
    print('else来た')

separate()

# tupleは編集不可
tuple1 = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# tuple1[1]からtuple1[9]まで2づつコピー
tuple2 = tuple1[1:9:2]

print(tuple2)
separate()
separate()
separate()

print('2018/06/30 Python3エンジニア認定試験合格')
