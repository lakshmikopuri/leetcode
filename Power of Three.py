#Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(20):
            if n==3**i:
                return True
                break
        else:
            return False
