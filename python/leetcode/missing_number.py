# https://leetcode.com/problems/missing-number/

def XorToN(n) : 
    if n % 4 == 0 : 
        return n
    if n % 4 == 1 : 
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        full_xor = XorToN (l)
        
        for num in nums:
            full_xor = full_xor^num
        return full_xor


        