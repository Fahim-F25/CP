n = int(input())   # number of levels
x = list(map(int, input().split()))[1:]  # ignore the first number (count)
y = list(map(int, input().split()))[1:]  # ignore the first number (count)

levels = set(x + y)   # combine both players' levels

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
