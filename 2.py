import random
#2.1
n = 10
m = 5
M1 = [[random.randint(0,50) for i in range(n)] for j in range(m)]#五行十列
M2 = [[random.randint(0,50) for i in range(m)] for j in range(n)]#五列十行
#2.2
def Matrix_multip(M1,M2):#两个矩阵相乘
    R=[[0 for i in range(5)] for j in range(5)]  # 五行五列
    for i in range(5):
        for j in range(5):
            sum=0
            for k in range(10):
                 sum += M1[i][k]*M2[k][j]#行*列
            R[i][j] = sum
        print(R[i])


Matrix_multip(M1,M2)