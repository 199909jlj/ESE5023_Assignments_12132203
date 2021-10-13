def Pascal_triangle(k):#帕斯卡三角函数
    n=0;
    p = [1]
    while n<k:
        n+=1
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]#调整每行数据
    print(p)#输出第K列的数值

Pascal_triangle(50)
Pascal_triangle(200)