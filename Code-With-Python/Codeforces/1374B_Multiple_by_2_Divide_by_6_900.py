t = int(input())
def mulDiv( num):
       movesNeed = 0
       while(num != 1):
              if num % 6 == 0:
                    num = num // 6
              else:
                     num = num * 2
              movesNeed = movesNeed + 1
              
              if num > 10**9:
                     return -1
      
       return movesNeed
        
for _ in range(t):
       n = int(input())
       result = mulDiv(n)
       print(result)
