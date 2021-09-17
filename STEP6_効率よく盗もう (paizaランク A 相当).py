#STEP6_効率よく盗もう (paizaランク A 相当).py

import decimal

# 有効数字10桁指定
decimal.getcontext().prec = 10

n,k = map(int,input().split())
W = [int(i) for i in input().split()]
V = [int(i) for i in input().split()]

left=0.0
right=5001.0
for i in range(50):
    mid = (left+right)/2
    tmp=[]
    for i in range(n):
        tmp.append(V[i]-(W[i]*mid))
    tmp = sorted(tmp , reverse = True)
    if sum(tmp[:k]) >= 0:
        left = mid
    else:
        right = mid

print(left)

