# https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """        
        writing_ptr, read_ptr = -1, -1

        i = 0

        while i < len(nums):
            if nums[i] == 0 : 
                writing_ptr = i
                break     
            i += 1
            

        while i < len(nums):
            if nums[i] != 0 : 
                read_ptr = i     
                break
            i += 1
        


        if(writing_ptr == -1  or read_ptr == -1):
            return nums
        
        while(read_ptr < len(nums)):
            # print(writing_ptr, read_ptr)
            if(nums[read_ptr] == 0):
                read_ptr += 1
            else:
                nums[writing_ptr] = nums[read_ptr]
                writing_ptr += 1
                read_ptr += 1

        while(writing_ptr < len(nums)):
            nums[writing_ptr] = 0
            writing_ptr+=1
        
        return nums
