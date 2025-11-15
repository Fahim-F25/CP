k, n, w = map(int,input().split())

totalCost = 0
for i in range(1,w+1):
    totalCost = totalCost + k*i

if totalCost > n:
    print(totalCost - n)
else:
    print(0)