t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    max_a = max(a)
    min_a = min(a)
    totalOperation = max_a - min_a
    print(totalOperation)

