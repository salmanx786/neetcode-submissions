class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_num = 0
        num_set = set(nums)

        for num in nums:
            number = 1
            if num - 1 in num_set:
                continue
            while num + number in num_set:
                number = number + 1
            if number > max_num:
                max_num = number
        return max_num
"""
Key Insight

The array is unordered, so you cannot skip elements by index.
Instead of trying to avoid recounting after traversing a sequence,
prevent it by only starting from sequence starts.

Recognition Checklist

When should I think of this pattern?

Input is an unsorted array.
Need to find consecutive numbers.
Need fast existence lookup.
Don't care about the original order.
Duplicates don't matter.

→ Convert to a Hash Set.
"""