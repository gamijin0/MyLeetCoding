#coding=utf-8
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Medium (32.13%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n5'
#
# Can you solve this problem? 🤔

#      /|
#     / |
#    /  |
#    -------
#       |  /
#       | /
#       |/
#
#
#

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start,end = 0,len(nums)-1

        while(start<end):
            mid = (start+end)/2
            if(nums[mid]==target):
                return mid
            if(nums[start]==target):
                return start
            if(nums[end]==target):
                return end
            if(nums[mid]>nums[start]):
                #left up
                if(target>nums[start] and target<nums[mid]):
                    end = mid
                else:
                    start = mid
            else:
                #right down
                if(target>nums[mid] and target<nums[end]):
                    start = mid
                else:
                    end = mid
        return -1

#if(__name__=="__main__"):
#    one = Solution()
#    print one.search([5,6,7,8,9,1,2,3,4],3)
