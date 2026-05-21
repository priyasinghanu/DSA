class Solution(object):
    def myPow(self, x, n):
        
        # Negative power handle
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n > 0:
            if n % 2 == 1:   # odd
                ans *= x

            x *= x
            n //= 2

        return ans