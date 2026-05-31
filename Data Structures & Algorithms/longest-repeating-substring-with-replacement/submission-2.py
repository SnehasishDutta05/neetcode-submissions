class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        end = 0 
        d = {}
        result = 0 
        flag = 0
        while(end<len(s) or flag == 1 ):
            if flag == 0:
                if(s[end] in d ):
                    d[s[end]] = d[s[end]] + 1 
                else:
                    d[s[end]] = 1 
            flag = 0
            length_sub_string = end - start + 1 
            max_occurence = 0 
            for key in d:
                if d[key] > max_occurence:
                    max_occurence = d[key]

            replacemet_required = length_sub_string - max_occurence
            if replacemet_required <= k:
                if length_sub_string > result:
                    result =  length_sub_string
            else:
                d[s[start]] -= 1
                start += 1
                flag = 1 
                continue  
            end += 1 
        return result

        