# Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # l=[]
        # for i in range(len(nums)):
        #     a=nums[i:i+3]
        #     if len(a)==3:
        #         result=1
        #         for i in a:
        #             result=result*i
        #         l.append(result)
        # return (max(l))
        nums.sort()
        n = len(nums)
        return max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])
         
