#coding=utf-8
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array
#
# Medium (38.59%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n1'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        for n in nums:

            res.append(n)
            res.sort(reverse=1)
            if(len(res)<=k):
                continue
            else:
                res = res[:k]

        return res.pop()
