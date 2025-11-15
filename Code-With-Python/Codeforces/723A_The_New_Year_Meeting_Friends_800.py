lis = list(map(int, input().split()))
lis.sort()

dis_x1 = lis[1] - lis[0]
dis_x3 = lis[2] - lis[1]

dis_total = dis_x1 + dis_x3

print(dis_total)