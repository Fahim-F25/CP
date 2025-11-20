# Unsolved
n = str(int(input()))
# count = 0

count = sum(n.count(c) for c in "47")  
if count == 4:
    print("YES")
elif count == 7:
    print('YES')
else:
    print("NO")  

