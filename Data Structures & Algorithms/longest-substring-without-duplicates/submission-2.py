class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        char_set = set()
        start = 0 
        max_length = 0 
        for end in range(len(s)):
            
            if s[end] in char_set: 
                while( result[0] != s[end]):
                        x = result.pop(0)
                        char_set.discard(x)
                x = result.pop(0) 
                char_set.discard(x) 
            else:
                char_set.add(s[end])  
            
            result.append(s[end])
            char_set.add(s[end])

            if len(result) > max_length:
                max_length = len(result)
        return max_length 

        