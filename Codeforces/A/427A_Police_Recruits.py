n = int(input())
police = 0
untreated = 0
event = list(map(int,input().split()))
for i in range(n):
    if event[i] == -1:
        if police > 0:
            police -= 1
        else:
            untreated += 1
    else:
        police += event[i]
        
print(untreated)
        