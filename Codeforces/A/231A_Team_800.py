n = int(input())  # number of rows
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# print(matrix[0])
# print(matrix[0].count(1))

ans = 0
for i in range(n):
  count = matrix[i].count(1)
  if count > 1: 
    ans = ans + 1
  
print(ans)
  