class Solution:
    def isPalindrome(self, s: str) -> bool:
            
        result = (''.join([ch for ch in s if ch.isalnum()])).lower()
        a = result[::-1]
        if result == "":
            return True
        elif result == a:
            return True
        else:
           return False
        
s = input()
print(Solution().isPalindrome(s))