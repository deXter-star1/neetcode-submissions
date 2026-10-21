class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_k_things = set()

        for i in range(len(nums)):
            if nums[i] in last_k_things:
                return True 
            else:
                last_k_things.add(nums[i])
                if len(last_k_things) > k:
                    last_k_things.remove(nums[i-k])
                    
        return False
        
    
        