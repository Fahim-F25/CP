from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # write in-place
                k += 1
        return k

nums = list(map(int, input().split()))
val = int(input())
k = Solution().removeElement(nums, val)
print(k)
print(nums[:k])  # optional: see the first k elements
