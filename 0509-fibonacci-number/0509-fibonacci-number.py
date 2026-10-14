class Solution:
    def fib(self, n: int) -> int:
        return self.f(n)

    def f(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.f(n-1) + self.f(n - 2)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna