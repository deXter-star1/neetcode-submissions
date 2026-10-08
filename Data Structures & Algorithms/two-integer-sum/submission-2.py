class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in h:
                return [h[diff], i]
            h[value] = i    
