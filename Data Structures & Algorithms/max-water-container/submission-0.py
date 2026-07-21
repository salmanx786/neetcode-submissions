class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1

        while left < right:
            right_height, left_height = heights[right], heights[left]
            area = (right - left) * min(left_height, right_height)
            result = max(area, result)
            if right_height > left_height:
                left += 1
            else:
                right -= 1
        return result
