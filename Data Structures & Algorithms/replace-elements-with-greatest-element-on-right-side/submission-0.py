class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #  arr = [2,4,5,3,1,2]
        greatest = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            current = arr[i]
            arr[i] = greatest 
            
            if current > greatest:
                greatest = current 
        return arr
        

        
            



        

