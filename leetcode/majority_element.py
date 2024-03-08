# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top_count = [(None,0),(None,0),(None,0)]
        
        top = [None,None,None]


        for num in nums:
            if num not in top:
                min_count = min(top_count, key = lambda x : x[1])
                
                top_count.remove(min_count)
                top_count.append((num,1))
                
                top.remove(min_count[0])
                top.append(num)
            else:
                this_element = [x for x in top_count if x[0] == num][0]
                top_count.remove(this_element)
                top_count.append((num,this_element[1] + 1))

        return((max(top_count, key = lambda x : x[1]))[0])

                

