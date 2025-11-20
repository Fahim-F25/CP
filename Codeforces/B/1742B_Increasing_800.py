t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = set(a)
    
    if len(a) == len(s):
        print("YES")
    else:
        print("NO")