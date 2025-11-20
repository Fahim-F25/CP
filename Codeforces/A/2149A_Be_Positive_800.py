t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    neg1 = arr.count(-1)
    zero = arr.count(0)

    opsForZero = 1 * zero  # each zero → 1 operation
    
    # operation for -1
    opsForNeg1 = 0
    if neg1 % 2 == 1:
        opsForNeg1 = opsForNeg1 + 2
    else:
        opsForNeg1 = 0
    
    totalOps = opsForNeg1 + opsForZero
    print(totalOps)
