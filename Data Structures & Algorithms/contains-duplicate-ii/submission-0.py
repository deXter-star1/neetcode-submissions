class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in d:
                closest_idx = d[nums[i]]
                if (i - closest_idx) <= k:
                    return True 
            d[nums[i]] = i

        return False