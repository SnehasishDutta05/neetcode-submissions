class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1 
            else:
                d[i] = 1 

        l = []
        for i in range(len(nums)+1):
            l.append([])

        for i in d :
            l[d[i]].append(i)
        
        result = []
        for i in range(len(l)-1,0,-1):
            if k > len(result) and len(l[i]) > 0 :
                result.extend(l[i])
                # k = k - len(l[i])
        return result

        


        