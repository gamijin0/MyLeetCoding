#coding=utf-8
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
#
# Medium (39.45%)
# Total Accepted:    147519
# Total Submissions: 373886
# Testcase Example:  '[1]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        if(len(nums)<=3):
            return min(nums)

        start = 0
        end = len(nums)-1
        if(nums[end]>nums[start]):
            return nums[start]

        while(start<end):
            mid = (start+end)/2
            if(mid==start):
                return min(nums[start],nums[end])
            if(nums[mid]>nums[start]):
                start=mid
            else:
                end = mid
        return nums[start]
