n = int(input())
notes = [100, 20, 10, 5, 1]
total = 0
for note in notes:
    total = total + ( n // note )
    n = n % note
print(total)
