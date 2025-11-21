class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        dec_a = int(a,2)
        dec_b = int(b,2)
        c = dec_a + dec_b # Sum of a and b in the form of integer
        
        bin_c = bin(c)[2:]    # convert the sum into binary
        
        return bin_c

a = input()
b = input()

print(Solution().addBinary(a,b))

