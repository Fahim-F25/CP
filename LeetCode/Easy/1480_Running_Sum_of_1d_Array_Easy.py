from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        runningSum = []
        for i in range(len(nums)):
            sum = sum + nums[i]
            runningSum.append(sum)
        return runningSum
    
nums = list(map(int, input().split()))
print(Solution().runningSum(nums))