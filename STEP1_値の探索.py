#二分探索メニュー 値の探索
#ソート済みの数列 A に 値 k が含まれているなら true を、含まれていないなら no を返す
def binary_search(a, n, k):
    #a : 数列, n : 数列のサイズ, k : 基準
    #// 探索範囲 [left, right]
    left = 0
    right = n-1
    
    #// 探索範囲を狭めていく
    while left <= right:

        #// 探索範囲の中央
        mid = (left + right) // 2

        if A[mid] == k:
            return True
        elif A[mid] < k:
            left = mid+1
        else:
            right = mid-1
    
    return False
    
n = int(input())
A = [int(i) for i in input().split()]
A.sort()

q = int(input())
for i in range(q):
    k = int(input())
    if binary_search(A,len(A),k) == True:
        print("Yes")
    else:
        print("No")
