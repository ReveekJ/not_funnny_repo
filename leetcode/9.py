class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = len(str(x))

        for i in range(n):
            f = x // (10 ** (n - i - 1)) % 10
            l = x // (10 ** i) % 10
            if f != l:
                return False
        return True
