class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        checker = None
        for i in range(len(nums)):
            if nums[i] > 0 :
                break
            start = i + 1 
            end = len(nums) - 1
            total = 0 - nums[i]
            if checker == nums[i]:
                continue
            else:
                checker = nums[i]
            while(start<end):
                if (nums[start] + nums[end] == total):
                    if (len(result) == 0 or result[-1] != [nums[i], nums[start] , nums[end]] ):
                        result.append([nums[i], nums[start] , nums[end]])
                    
                    end -= 1 

                elif (nums[start] + nums[end] > total):
                    end -= 1 
                else :
                    start += 1 
        return result



            
        