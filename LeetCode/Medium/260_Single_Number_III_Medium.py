from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sn_list = []
        counts = Counter(nums)
        for num, freq in counts.items():
            if freq == 1:
                sn_list.append(num)
        return sn_list
            
nums = list(map(int,input().split()))
print(Solution().singleNumber(nums))
            
            
            