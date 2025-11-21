from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2  # total Sum of 0..n numbers
        sumOfNums = sum(nums) # Total sum of nums in the given list
        
        return total - sumOfNums
        
    
nums = list(map(int,input().split()))
print(Solution().missingNumber(nums))
            