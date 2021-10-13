import random
from functools import reduce
#暂存操作数
operator = {1: '+', 2: '-', 0: ''}
#暂存1-9数字
base = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def Find_expression(n):
    total = 3 ** 8
    for i in range(total):#循环遍历获取所有运算式
        num=i
        # 转化为8位3进制数，得到运算符数组
        arr = []
        for index in range(8):
            index = 7 - index
            arr.append(num // (3 ** index))
            num -= (num // (3 ** index)) * (3 ** index)
        arr = map(lambda x: operator[x], arr)

        # 生成表达式
        expression = reduce(lambda x, y: x + y, zip(base, arr))
        expression = list(expression)
        expression.append('9')
        expression = ''.join(expression)
        # 计算表达式结果
        res = eval(expression)
        if res == n:#若是符合条件就输出结果
            print('{0} = {1}'.format(expression,n))

n=random.randint(1,100)
Find_expression(n)