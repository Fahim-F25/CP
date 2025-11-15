s = input()

l = set(s.strip("{} ").replace(" ",""))

if s == '{}':
    print(0)
elif len(s) == 3:
    print(1)
else:
    print(len(l)-1)
