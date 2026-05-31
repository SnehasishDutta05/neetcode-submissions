class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0 
         
        for i in s:
            if i - 1 not in s :
                length = 1 
                while i + 1 in s :
                    length += 1
                    i = i +1 
                longest = max(longest, length)
        return longest
            
                

        