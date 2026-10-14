class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        ins = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[ins] = nums[i]
                ins += 1
        return ins

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna