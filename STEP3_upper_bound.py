##二分探索メニュー upper_bound
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
A = [int(i) for i in input().split()]
A.sort()

q = int(input())
for i in range(q):
    k = int(input())
    print(len(A)-binary_search(A,len(A),k+1))
