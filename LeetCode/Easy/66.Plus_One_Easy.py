from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for item in digits:
            num = num * 10 + item
        
        inNum = num + 1
        
        result = []
        while inNum > 0:
            result.append(inNum % 10)
            inNum = inNum // 10
            
        result.reverse()
        return result
            

digits = list(map(int,input().split()))
print(Solution().plusOne(digits))

