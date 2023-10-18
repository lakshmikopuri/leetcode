#Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range((n)):
            if n==3**i:
                return True
                break
        else:
            return False
