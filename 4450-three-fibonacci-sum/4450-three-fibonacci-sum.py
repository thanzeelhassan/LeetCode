class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        # Fibonacci numbers : 0 1 1 2 3 5 8 13 21 34 55 
        # Sums : 2 4 6 10 16 26 42 68 110 

        # divide n by 2
        # check if result is a fibonacci number

        def is_perfect_square(x):
            s = int(math.sqrt(x))
            return s * s == x

        def is_fibonacci(n):
            return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

        if n % 2 == 0:
            return is_fibonacci(n//2)
        return False
