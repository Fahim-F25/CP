s = str(input())
numbers = []

for x in s:
       if x.isdigit():
              numbers.append(x)
              
numbers.sort()

for i in range(len(numbers)):
       
    if i == len(numbers) - 1:
        print(numbers[i], end='')   # last number, no '+'
    else:
        print(f"{numbers[i]}+", end='')

