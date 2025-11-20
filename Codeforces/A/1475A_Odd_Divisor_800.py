t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())
    if n & (n - 1) == 0:  # check if n is power of 2
        print("NO")
    else:
        print("YES")
