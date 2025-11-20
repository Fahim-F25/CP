# # a, b, c = map(int, input().split())

# # e = a + b * c
# # f = a * (b + c)
# # g = a * b * c
# # h = (a + b) * c

# # s = [e,f,g,h]

# # print(max(s))

# a, b, c = map(int, input().split())
# print(max(a+b*c, a*(b+c), a*b*c, (a+b)*c, a+b+c))


# Codeforces 479A - Expression

a = int(input())
b = int(input())
c = int(input())

# Try all possible valid expressions
results = [
    a + b + c,
    a * b * c,
    (a + b) * c,
    a * (b + c)
]

print(max(results))
