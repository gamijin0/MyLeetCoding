#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray
#
# Medium (25.21%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# 
# 
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCache = [0 for i,v in enumerate(nums)]
        minCache = [0 for i,v in enumerate(nums)]
        
        maxCache[0] = nums[0]
        minCache[0] = nums[0]
        result = nums[0]

        for i,v in  enumerate(nums):
            if(i==0):
                continue
            else:
                maxCache[i] = v
                minCache[i] = v
            if(v>0):
                maxCache[i] = max(maxCache[i],maxCache[i-1]*v)
                minCache[i] = min(minCache[i],minCache[i-1]*v)
            elif(v<0):
                maxCache[i] = max(maxCache[i],minCache[i-1]*v)
                minCache[i] = min(minCache[i],maxCache[i-1]*v)

            result = max(result,maxCache[i])

        return result



