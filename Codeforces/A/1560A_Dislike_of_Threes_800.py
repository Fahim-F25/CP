t = int(input())
nums = []
for i in range(1,1000+1):
    if i % 3 != 0 and i % 10 != 3:
        nums.append(i)
        
for _ in nums:
    k = int(input())
    print(nums[k-1])