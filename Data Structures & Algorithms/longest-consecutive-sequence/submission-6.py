class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest = 1
        count = 1

        for i in range(1, len(nums)):

            # Ignore duplicate numbers
            if nums[i] == nums[i - 1]:
                continue

            # Consecutive number found
            elif nums[i] == nums[i - 1] + 1:
                count += 1

            # Sequence is broken
            else:
                longest = max(longest, count)
                count = 1

        # Check the last sequence
        longest = max(longest, count)

        return longest