#STEP9_長い長い数列.py

n=int(input())
A=[int(i) for i in input().split()]
m=int(input())
B=[int(i) for i in input().split()]
k=int(input())

B=sorted(B)

def binary_search(a,n, k):
#a : 数列, n : 数列のサイズ, k : 基準
    #// 探索範囲 [left, right]
    left = 0
    right = n
    
    #// 探索範囲を狭めていく
    while left < right:
        #// 探索範囲の中央
        mid = (left + right) // 2

        if a[mid] < k:
            #// a[0] ~ a[mid] は k 未満なので調べる必要が無い
            left = mid+1
        else:
            right = mid
    
    return right

left=-1
right=200000000

while(right-left >1):
    mid = (left+right)//2
    smaller=0
    for i in range(n):
        upper = binary_search(B,len(B),A[i]+mid+1)
        lower = binary_search(B,len(B),A[i]-mid)
        smaller += upper -lower
    
    if smaller <k:
        left=mid
    else:
        right=mid

print(right)

