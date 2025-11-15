n = int(input())

arr = []

for i in range(n):
    s = input().upper()
    arr.append(s)

# Count how many times each string appears
from collections import Counter

counts = Counter(arr)

# Find the most common string
winnerTeam = counts.most_common(1)[0][0]

print(winnerTeam)
