from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num, freq in counts.items():
            if freq == 1:
                return num
                

nums = list(map(int, input().split()))
print(Solution().singleNumber(nums))
        
