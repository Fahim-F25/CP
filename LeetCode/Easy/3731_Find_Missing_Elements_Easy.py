from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = min(nums)
        b = max(nums)
        arr = []
        for i in range(a,b+1):
            arr.append(i)
        
        result = []
        for i in arr:
            if i not in nums:
                result.append(i)
        
        return result
        
nums = list(map(int, input().split()))
print(Solution().findMissingElements(nums))
