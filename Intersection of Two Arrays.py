#Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1,num2=set(nums1),set(nums2)
        l=[]
        for i in num1:
            if i in num2:
                l.append(i)
        return l
