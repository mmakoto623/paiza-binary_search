#STEP7_太巻きを分けよう(おなかペコペコ)(paizaランクA相当).py
L,n,k = map(int,input().split())

a=[0]*(k+1)
A=input().split()
for i in range(1,len(A)+1):
    a[i]=int(A[i-1])
a.append(L)

left=0
right=L+1
while (right-left>1):
    mid = (left+right) //2
    last_index=0
    parts=0
    for i in range(len(a)):
        if (a[i] - a[last_index]) >= mid:
            parts+=1
            last_index=i
    
    if parts<n:
        right = mid
    else:
        left = mid

print(left)
