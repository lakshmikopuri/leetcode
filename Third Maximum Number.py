#Third Maximum Number
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=set(nums)
        if len((num))>=3:
            l=sorted(num)
            return l[-3]
        else:
            return (max(num))
