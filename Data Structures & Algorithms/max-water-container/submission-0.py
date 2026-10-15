class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  height = [1,7,2,5,4,7,3,6]
        l = 0
        r = len(heights)-1
        max_area = 0

        while l < r:
            width = r - l
            min_height = min(heights[l], heights[r])
            area = width * min_height

            if area > max_area:
                max_area = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area

        

