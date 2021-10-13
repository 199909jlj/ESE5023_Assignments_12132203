import random

def Print_values(a,b,c):
    #输出a,b,c，实际上是从大到小按顺序输出
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(c,a,b)
        else:
            print(c,b,a)

a=random.random()#获取随机数
b=random.random()
c=random.random()
Print_values(a,b,c)