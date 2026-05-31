class Solution:
    def findMin(self, nums: List[int]) -> int:
        # flag = 0
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range (len(nums) - 1 ):
        #     if nums[i+1] < nums[i]:
        #         return nums[i+1]
        # return nums[0]
        l = 0 
        r = len(nums) - 1 
        while (l<r):
            temp = (l+r) 
            m = temp //2
           
            if nums[m] > nums [r]:
                l = m + 1
            else :
                r = m 
        return nums[l]
            
        