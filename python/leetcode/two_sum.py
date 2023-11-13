# https://leetcode.com/problems/two-sum/


def tuple_sort(t):
    return t[0]


class Solution(object):
    def twoSum_indexmapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_list = []
        for index in range(len(nums)):
            index_list.append((nums[index], index))

        index_list.sort(key=tuple_sort)

        left = 0
        right = len(nums) - 1
        
        while(left < right):
            
            sum = index_list[left][0]  + index_list[right][0]
            if(sum == target) : 
                return [index_list[left][1], index_list[right][1]]
            elif (sum < target) :
                left = left + 1
            else:
                right = right - 1

    def twoSum(self, nums, target):
        
        index_dict = {}
        for index in range(len(nums)):
            index_dict[nums[index]] = index
        
        for i in range(len( nums)) : 
            num = nums[i]
            reminder = target - num
            if(reminder in index_dict) and (index_dict[reminder] != i): 
                return(i, index_dict[reminder])
        