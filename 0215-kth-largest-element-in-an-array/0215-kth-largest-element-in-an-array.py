class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k -1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna