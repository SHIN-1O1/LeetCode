class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
            
        prev2 = 0  
        prev1 = 1 
        
        current = 0
        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna