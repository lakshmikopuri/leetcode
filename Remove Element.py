#Remove Element
lass Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1  
        while i >= 0:
            if val == nums[i]:
                del nums[i]
            i -= 1
        print(nums)
