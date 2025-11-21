class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            index = haystack.find(needle)
        else:
            return -1
            
        return index
                
a = input()
b = input()
c = Solution().strStr(a,b)
print(c)