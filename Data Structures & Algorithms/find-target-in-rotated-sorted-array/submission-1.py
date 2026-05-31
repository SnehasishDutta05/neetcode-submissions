class Solution:
    def binnary(self , nums , l , r , target ):
        while(l<=r):
            m = (l+r) //2
            if nums[m] == target:
                return m
            elif nums[m]>target:
                r = m - 1 
            else:
                l = m + 1 
        return -1 



    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        while (l<r):
            temp = (l+r) 
            m = temp //2
           
            if nums[m] > nums [r]:
                l = m + 1
            else :
                r = m 
        cut = nums[l]
        if target >= nums[l] and target <= nums[-1]:
            result = self.binnary(nums , l , len(nums) -1 , target)
        else:
            result = self.binnary(nums , 0 , l - 1  , target)
        return result


