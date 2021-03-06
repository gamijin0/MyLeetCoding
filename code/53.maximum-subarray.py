#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# Easy (39.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]


        maxSum = float('-inf') 
        tempSum = 0

        i=0
        while(i<len(nums)):
            tempSum+=nums[i]
            if(tempSum>maxSum):
                maxSum = tempSum
            if(nums[i]>=0):
                i += 1
                continue
            else:
            # when nums[i] < 0
                if(tempSum<0):
                    tempSum=0
            i += 1

        return maxSum



