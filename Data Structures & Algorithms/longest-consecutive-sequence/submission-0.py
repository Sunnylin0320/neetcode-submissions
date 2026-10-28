class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        longest = 1
        length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                length = 1
            longest = max(longest, length)

        return longest