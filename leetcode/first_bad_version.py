# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# import isBadVersion
# isBadVersion function is provided by leetcode

def firstBadVersionHelper(left, right):

    if(left==right) : return left

    mid = (left + right) / 2
    if(isBadVersion(mid)):
        return firstBadVersionHelper(left,mid)
    else:
        return firstBadVersionHelper(mid+1,right)


class Solution:

    
    
    def firstBadVersion(self, n: int) -> int:

        return firstBadVersionHelper (0,n-1)
        
        

            
            
            

        