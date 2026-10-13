class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0

        for n in numSet:
            #look for the initiator value
            if n-1 not in numSet:
                curr_num = n
                curr_len = 1
                while curr_num + 1 in numSet:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
        return max_len        

      
              
