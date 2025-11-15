t = int(input())
a = 'codeforces'

def differ(s):
       count = 0
       for x in range(len(a)):
              if a[x] != s[x]:
                  count += 1
       return count

for _ in range(t):
       s = input()
       print(differ(s))
