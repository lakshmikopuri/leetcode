#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num = sum(int(i) for i in str(num))
        return num
