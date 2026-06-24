class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        maxp = nums[0]
        minp = nums[0]

        for i in range(1,len(nums)):
            if nums[i] >= 0:
                maxp = max(nums[i], maxp*nums[i])
                minp = min(nums[i], minp*nums[i])

            else:
                temp = maxp
                maxp = max(nums[i], minp*nums[i])
                minp = min(nums[i], temp*nums[i])
            result = max(result,maxp)
        return result