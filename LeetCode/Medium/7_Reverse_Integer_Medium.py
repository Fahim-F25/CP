class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x) # absolute valu [no negative sign]
        rev_x = 0

        while x != 0:
            rem = x % 10
            x //= 10
            rev_x = rev_x * 10 + rem

        rev_x *= sign

        # Check 32-bit integer range
        if rev_x < -2**31 or rev_x > 2**31 - 1:
            return 0

        return rev_x

x = int(input())
print(Solution().reverse(x))