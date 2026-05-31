class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 :
            return False
        queue = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                queue.append(i)
            elif i == ')':
                if(len(queue)== 0 or queue[-1] != '('):
                    return False
                    
                else:
                    queue.pop(-1)
                    

            elif i == '}':
                if(len(queue)== 0 or queue[-1] != '{' ):
                    return False
                else:
                    queue.pop(-1)
                    
            elif i == ']':
                if(len(queue)== 0 or queue[-1] != '[' ):
                    return False
                else:
                    queue.pop(-1) 
            else:
                return False 
        if len(queue) == 0:
            return True
        else:
            return False


        