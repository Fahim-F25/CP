n = int(input())

while True:
   n = n + 1
   if len(str(n)) != len(set(str(n))):
     continue
   else:
     print(n)
     break
      
      

  
