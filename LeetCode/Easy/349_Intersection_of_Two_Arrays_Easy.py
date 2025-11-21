from typing import List
1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
    
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))

print(Solution().intersection(nums1,nums2))