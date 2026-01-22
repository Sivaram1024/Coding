class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        
        arr_sum = n * (n+1) // 2
        actual_sum = sum(arr)
        
        missing_array = arr_sum - actual_sum
        return missing_array