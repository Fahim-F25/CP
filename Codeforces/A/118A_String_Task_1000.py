s = input()
vowels =  "aeiouyAEIOUY"
for char in vowels:
    s = s.replace(char, "")
# print(s.lower())



for i in range(len(s)):
   print('.' + s[i].lower(),end='')



