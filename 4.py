import random
def Least_moves(n):
    sum=n#令总值为金币的计算和
    count=0
    while sum>1:#循环直到一个硬币为止
        count+=1
        if sum%2== 1:#判断当前金钱是否是奇数，是奇数则减去一
            sum=sum-1
        else:#偶数就除以2
            sum=sum/2
    return count

n=random.randint(1,100);
print('n:{0}'.format(n))
print(Least_moves(n))
