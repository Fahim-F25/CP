from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None: 
        n = nums.sort()
        # print(n)
        return n
nums = list(map(int, input().split()))
print(Solution().sortColors(nums))