class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        curr = max_water = 0
        while left < right:
            if height[right] > height[left]:
                curr = height[left] * (right - left)
                max_water = max(curr,max_water)
                left+=1
            else:
                curr = height[right] * (right - left)
                max_water = max(curr,max_water)
                right-=1
        return max_water


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna