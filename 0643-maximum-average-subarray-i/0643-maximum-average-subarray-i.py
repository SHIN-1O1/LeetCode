class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = sum(nums[:k])
        max_sum = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            max_sum = max(curr, max_sum)
        return max_sum/k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna