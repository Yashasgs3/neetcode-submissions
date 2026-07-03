class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):

            # Ignore duplicate numbers
            if nums[i] == nums[i - 1]:
                continue

            # Consecutive number found
            elif nums[i] == nums[i - 1] + 1:
                current += 1

            # Sequence is broken
            else:
                longest = max(longest, current)
                current = 1

        # Check the last sequence
        longest = max(longest, current)

        return longest