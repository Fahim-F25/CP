n , k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k-1]

count = 0
for i in scores:
    if i >= threshold and i > 0:
        count += 1


print(count)  



