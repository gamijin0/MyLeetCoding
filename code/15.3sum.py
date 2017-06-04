#coding=utf-8
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.49%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
# 
# Note: The solution set must not contain duplicate triplets.
# 
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# S,sort() ==>> [-4, -1, -1, 0, 1, 2]
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()

        if(len(nums)<=2):
            return []
        if(len(nums)==3):
            if(sum(nums)==0):
                return [nums]
            return []

        res = []
        first = 0
        second = 1
        third = len(nums)-1
        while(first<len(nums)-2):
            while(first<len(nums)-2 and first>0 and nums[first]==nums[first-1]):
                first+=1
            second = first+1
            third = len(nums)-1
            while(second<third):
                while(second<third and second>first+1 and nums[second]==nums[second-1]):
                    second+=1
                while(third>second and third<len(nums)-1 and nums[third]==nums[third+1]):
                    third-=1

                if(second>=third):
                    break
                if(sum([nums[first],nums[second],nums[third]])==0):
                    res.append([nums[first],nums[second],nums[third]])
                    second+=1
                    third-=1
                else:
                    if(sum([nums[first],nums[second],nums[third]])<0):
                        second+=1
                    else:
                        third-=1
            first+=1
        return res
if(__name__=="__main__"):
    one = Solution()
    a = [-2,0,0,2,2]
    print one.threeSum(a)
