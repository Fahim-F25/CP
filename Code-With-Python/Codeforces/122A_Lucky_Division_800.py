n = int(input())

lucky_numbers = [4, 7, 44, 47, 74, 77,
                 444, 447, 474, 477,
                 744, 747, 774, 777]

for x in lucky_numbers:
    if n % x == 0:
        print("YES")
        break
else:  # This runs only if loop completes without break
    print("NO")
    


