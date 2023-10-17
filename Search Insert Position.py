#Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int):
        for i in range(len(nums)):
            if nums[i]==target:
                k= nums.index(nums[i])
                return k
            elif (nums[i]>target):
                return i
        return len(nums)  
