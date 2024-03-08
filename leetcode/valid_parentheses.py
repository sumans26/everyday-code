# https://leetcode.com/problems/valid-parentheses/

from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()

        paren_map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for e in s:
            
            if (e in paren_map):
                if(len(stack) == 0):
                    return False
                elif (stack.pop() == paren_map[e]):
                    continue
                else:
                    return False

            elif(e in {'(', '{', '['}):
                stack.append(e)
            
            else:
                return False
        
        return(len(stack) == 0) 




        