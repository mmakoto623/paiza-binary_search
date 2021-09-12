#二分探索メニュー Final「ある範囲に含まれている整数の個数」
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

n = int(input())
A = map(int,input().split())
q = int(input())

A = sorted(A)


for i in range(q):
    l,r = map(int,input().split())
    res1 = binary_search(A,len(A),l)
    res2 = binary_search(A,len(A),r+1)
    print(res2-res1)
