n = int(input())

s = input().upper()

countA = s.count("A")
countD = s.count("D")

if countA > countD:
    print("Anton")
elif countD > countA:
    print("Danik")
else:
    print("Friendship")