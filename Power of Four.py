#Power of Four
#Given an integer n, return true if it is a power of four. Otherwise, return false. An integer n is a power of four, if there exists an integer x such that n == 4x.
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(20):
            if n==4**i:
                return True
                break
        else:
            return False
