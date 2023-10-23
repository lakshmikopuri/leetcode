#Longest Uncommon Subsequence I
#Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b :
            return -1
        else:
            if len(a)>len(b):
                return len(a)
            else:
                return len(b)
