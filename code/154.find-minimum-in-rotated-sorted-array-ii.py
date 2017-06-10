#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
#
# Hard (36.81%)
# Total Accepted:    77000
# Total Submissions: 209155
# Testcase Example:  '[1]'
#
# 
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# 
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
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
        mid = (start+end)/2

        if(nums[start]<nums[end]):
            return nums[start]

        if(nums[start]==nums[end]==nums[mid]):
            return min(
                    self.findMin(nums[start:mid]),
                    self.findMin(nums[mid:end+1])
                    )

        if(nums[start]<=nums[mid]):
            return min(
                    nums[start],
                    self.findMin(nums[mid:end+1])
                    )
        if(nums[mid]==nums[end]):
            return self.findMin(nums[start:mid+1])
        
        if(nums[mid]<nums[start]):
            return self.findMin(nums[start:mid+1])

        


if(__name__=="__main__"):
    one = Solution()
    print one.findMin([2,0,1,1,1])
