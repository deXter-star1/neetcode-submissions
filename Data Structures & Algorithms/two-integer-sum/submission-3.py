class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        h = {}   
        for i, value in enumerate(nums):
            diff = target - value
            if diff in h:
                return [h[diff], i]
            h[value] = i    