t = int(input())  # number of test cases

for _ in range(t):
    s = input().strip()  # 6-digit string
    first_sum = int(s[0]) + int(s[1]) + int(s[2])
    last_sum = int(s[3]) + int(s[4]) + int(s[5])
    
    if first_sum == last_sum:
        print("YES")
    else:
        print("NO")
