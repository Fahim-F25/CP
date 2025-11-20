n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
totalSum = sum(a)
mySum = 0
for i in range(n):
    mySum = mySum + a[i]
    if mySum > totalSum - mySum :
        print(i + 1)
        break
    else :
        continue
   
        

