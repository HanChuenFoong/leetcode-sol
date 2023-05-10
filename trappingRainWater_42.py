from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while (l < r):
            if (leftMax < rightMax):
                l += 1
                leftMax = max(leftMax, height[l])  # Compare and update the latest left maximum
                res += leftMax - height[l] # Add volume of water to res. RHS will always result 0 and above (positive #)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
x = sol.trap(height)
print(x)