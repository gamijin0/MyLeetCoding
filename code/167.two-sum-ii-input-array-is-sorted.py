#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
# Easy (47.15%)
# Total Accepted:    76251
# Total Submissions: 161749
# Testcase Example:  '[2,3,4]\n6'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(numbers)<=1):
            return None
        if(len(numbers)==2 and sum(numbers)==target):
            return [1,2]
        f = 0
        b = len(numbers)-1

        while(f<b):
            if(numbers[f]+numbers[b]<target):
                f+=1
                while(f>0 and f<b and numbers[f-1]==numbers[f]):
                    f+=1
            if(numbers[f]+numbers[b]>target):
                b-=1
                while(b<len(numbers)-1 and b>f and numbers[b+1]==numbers[b]):
                    b-=1
            if(numbers[f]+numbers[b]==target):
                return [f+1,b+1]

        return None
