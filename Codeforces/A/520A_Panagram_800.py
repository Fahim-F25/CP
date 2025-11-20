n = int(input())
s = input().lower()
letters = 'abcdefghijklmnopqrstuvwxyz'

for letter in letters:
    if letter not in s:
        print("NO")
    else:
        print("YES")

