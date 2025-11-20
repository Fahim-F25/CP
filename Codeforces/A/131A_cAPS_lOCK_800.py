s = input()
if len(s)==1 and s.islower():
    print(s.upper()) 
elif s.isupper():
    print(s.lower())
elif s[0].islower() and s[1:].isupper():
    print(s.capitalize())
else:
    print(s)
    
    