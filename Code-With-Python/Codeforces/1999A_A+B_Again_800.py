t = int(input())

def sumOfDigit( num):
    sumOfDigits = 0
    while(num > 0):
        rem = num % 10
        num = num // 10
        sumOfDigits = sumOfDigits + rem

    return sumOfDigits


for _ in range(t):
   num = int(input())
   print(sumOfDigit(num))
    
    
    
    