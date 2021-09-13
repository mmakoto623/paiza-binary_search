#STEP5_パイプを切り出そう

import decimal

# 有効数字10桁指定
decimal.getcontext().prec = 10

n,k = map(int,input().split())
A=[int(i) for i in input().split()]

left=0
right=10001.0
for i in range(100):
    mid = (left+right)/2
    num_of_pipes = 0
    for j in A:
        num_of_pipes += j//mid
    
    if num_of_pipes < k:
        right = mid
    else:
        left = mid
        
print(left)
