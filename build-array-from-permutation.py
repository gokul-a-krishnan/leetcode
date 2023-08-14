from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


sol = Solution()
print(sol.buildArray([0, 2, 1, 5, 3, 4]))
