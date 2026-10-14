class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        # arr = [10,9,1,1,1,2,3,1]
        if len(arr) > 1:
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]

            self.sortArray(left_arr)
            self.sortArray(right_arr)

            i = 0 #left arrray index
            j = 0  #right array index
            k = 0 #merged array index

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                else: 
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
        return arr
        