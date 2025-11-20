# TLE 
# n , k = map(int,input().split())
# a = []
# b = []
# for i in range(1,n+1):
#     if i % 2 != 0:
#         a.append(i)
#     else:
#         b.append(i)

# # print(a)
# # print(b)
# c = a + b
# # print(c)

# print(c[k-1])


# TLE Free code
n, k = map(int, input().split())

odd_count = (n + 1) // 2

if k <= odd_count:
    print(2 * k - 1)
else:
    print(2 * (k - odd_count))
