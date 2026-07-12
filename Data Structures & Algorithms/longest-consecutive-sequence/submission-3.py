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
