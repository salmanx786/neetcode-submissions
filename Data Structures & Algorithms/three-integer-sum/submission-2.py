class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        result = []
        for num in nums:
            right = len(nums) - 1
            left = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum == 0:
                    result.append([num, nums[left], nums[right]])

                if sum > 0:
                    right -= 1
                    continue
                elif sum < 0:
                    left += 1
                    continue
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            i += 1
        return result


    """3Sum — Notebook Summary

Pattern: Sorting + Two Pointers

Recognition:

Find 3 numbers with a target sum.
Return unique triplets.

Core Idea:

Sort the array.
Fix one number.
Remaining problem becomes Two Sum (target - fixed).
Use two pointers on the remaining array.

Why sort?

Sorting tells you which pointer to move:
Sum too small → left++
Sum too large → right--

Duplicate Handling:

Skip duplicate fixed values (same triplets would be found again).
After finding a triplet, skip duplicate left and right values (same triplet within the current search).

Time Complexity:

Sorting: O(n log n)
Two pointers for each fixed number: O(n²)
Overall: O(n²)
Mental Model

3Sum = Sort → Fix one number → Solve Two Sum → Skip duplicates."""
