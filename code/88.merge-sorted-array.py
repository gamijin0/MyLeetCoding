#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array
#
# Easy (31.82%)
# Total Accepted:    162569
# Total Submissions: 510809
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        n1 = nums1[0:m]
        n2 = nums2
        i = m
        j = n
        
        while( i > 0 and j > 0):
            if(n1[-1*i] < n2[-1*j]):
                nums1[count] = n1[-1*i]
                i-=1
            else:
                nums1[count] = n2[-1*j]
                j-=1
            count+=1

        if(i>0):
            nums1[count:]=n1[-1*i:m]
        if(j>0):
            nums1[count:]=n2[-1*j:n]

