# https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) -1
        mid = int((left + right) / 2)

        while left <= right : 
            if(nums[mid] == target):
                return mid
            elif (target < nums[mid]):
                right = mid - 1
            else : 
                left = mid + 1

            mid = int((left + right) / 2)
        
        return -1
        


