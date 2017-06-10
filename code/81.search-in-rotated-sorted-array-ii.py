#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#
# Medium (32.81%)
# Total Accepted:    92503
# Total Submissions: 281955
# Testcase Example:  '[]\n5'
#
# 
# Follow up for "Search in Rotated Sorted Array":
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
# Write a function to determine if a given target is in the array.
# 
# The array may contain duplicates.
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        if not nums:
            return False

        start,end = 0,len(nums)-1

        if(nums[start]==target):
            return True 
        if(nums[end]==target):
            return True 

        while(start<end):
            mid = (start+end)/2
            if(nums[mid]==target):
                return True 
            if(nums[start]==target):
                return True 
            if(nums[end]==target):
                return True 
            if(mid==start or mid==end):
                break
            if(nums[mid]==nums[start]==nums[end]):
                return self.search(nums[start:mid],target) or self.search(nums[mid:end+1],target)
            if(nums[mid]==nums[start]):
                start = mid
                continue
            if(nums[mid]==nums[end]):
                end = mid
                continue

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
        return False

#if(__name__=="__main__"):
#    one = Solution()
#    print one.search([5,6,7,8,9,1,2,3,4],3)
