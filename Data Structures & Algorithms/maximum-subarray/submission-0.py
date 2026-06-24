class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_num = nums[0]

        for i in range(1,len(nums)):
            current = max(nums[i], current+nums[i])
            max_num = max(max_num, current)
        return max_num