from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


print(Solution().getConcatenation([1, 2, 3, 4, 5]))
