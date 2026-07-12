class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1


"""If the data is sorted, ask yourself:
"Can the order tell me which 
direction to move instead of 
checking every possibility?
Two Sum II
Pattern

Two Pointers (Sorted Array)

Recognition Checklist

Think of this pattern when you see:

Array is sorted
Need to find a pair
Looking for a target sum
O(1) extra space

Two pointers from opposite ends.
"""
