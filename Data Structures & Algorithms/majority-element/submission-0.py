class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        n = len(nums)

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        
        for num, freq in h.items():
            if freq > n/2:
                return num
            
                
            
        


        
            
            

            
                