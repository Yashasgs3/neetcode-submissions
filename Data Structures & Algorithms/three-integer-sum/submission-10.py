
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            seen = set()

            for j in range(i+1,len(nums)):

                third = -(nums[i]+nums[j])
                if third in seen:
                    triplet = tuple(sorted([nums[i],nums[j],third]))
                    result.add(triplet)
                seen.add(nums[j])
        return [list(triplets) for triplets in result]

        