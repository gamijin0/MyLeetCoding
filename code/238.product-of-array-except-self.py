#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self
#
# Medium (48.40%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,0]'
#
# 
# Given an array of n integers where n > 1, nums, return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array
# does not count as extra space for the purpose of space complexity analysis.)
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if(len(nums)==1):

            return [0]

        elif(len(nums)==2):

            return nums[::-1]

        

        left = []

        

        

        for i,v in enumerate(nums):

            if(i==0):

                left.append(1)

            else:

                left.append(left[i-1]*nums[i-1])

        

        temp = 1

        for i,v in enumerate(nums[::-1]):

            if(i==0):

                temp=1

            else:

                temp*=nums[-1*(i-1)-1]

                left[-1*(i)-1]*=temp

        

        return left


#if(__name__=="__main__"):
#    one = Solution()
    #print one.productExceptSelf([1,2,3,4])

        # [3,2,5,8]

        

        # [1,1*3,1*3*2,1*3*2*5]

        # [2*5*8*1,5*8*1,8*1,1]

        

        
