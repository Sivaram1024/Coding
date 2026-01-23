class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums_sum = n * (n+1) // 2
        actual_sum = sum(nums)

        missing = nums_sum - actual_sum
        return missing