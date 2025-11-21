class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        
        return len(l[-1])
    
s = input()
print(Solution().lengthOfLastWord(s))
        