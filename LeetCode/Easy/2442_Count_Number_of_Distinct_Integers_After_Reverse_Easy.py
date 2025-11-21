from typing import List
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev_numbers = []
        for n in nums:
            revNum = 0
            while n != 0:
                rem = n % 10
                n = n // 10
                revNum = revNum * 10 + rem 
            rev_numbers.append(revNum)
            
        nums.extend(rev_numbers)
        return len(set(nums))
    
nums = list(map(int,input().split()))
print(Solution().countDistinctIntegers(nums))