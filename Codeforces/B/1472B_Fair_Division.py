t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count1 = a.count(1) * 1
    count2 = a.count(2) * 2
    totalCount = count1 + count2
    
    if totalCount % 2 != 0:
        print("NO")
    else:
        half = totalCount // 2
        if half % 2 != 0 and count1 == 0:
            print("No")
        else:
            print("YES")