#STEP8_太巻きを分けよう(おなかいっぱい)(paizaランクA相当).py
L,n,k = map(int,input().split())

a=[0]*(k+1)
A=input().split()
for i in range(1,len(A)+1):
    a[i]=int(A[i-1])
a.append(L)

left=1
right=L
for i in range(1,len(a)):
    left = max(left,a[i]-a[i-1])
left -=1

while((right-left) > 1):
    mid = (left+right)//2
    last_index =0
    index=0
    parts=0
    while(True):
        while(index+1<len(a) and ((a[index+1]-a[last_index]) <= mid)):
            index+=1
        parts+=1
        if index == (len(a) -1):
            break
        last_index = index
    
    if parts > n:
        left = mid
    else:
        right= mid

print(right)
