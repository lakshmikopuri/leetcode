#Number Complement
#The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
class Solution:
    def findComplement(self, num: int) -> int:
        k = bin(num)[2:]
        a = ""
        for i in k:
            if i == "1":
                a+= "0"
            else:
                a+= "1"
        return int(a, 2)
        
