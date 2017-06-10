#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
#
# Medium (35.60%)
# Total Accepted:    115324
# Total Submissions: 323975
# Testcase Example:  '[]'
#
# 
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=2):
            return len(nums)
        
        count = 0
        prev = None
        i = 0

        while(i<len(nums)):
            if(prev==None):
                count=1
                prev = nums[i]
                i += 1
                continue
            if(nums[i]==prev):
                count+=1
                if(count==3):
                    del nums[i]
                    count -= 1
                    continue
            else:
                prev = nums[i]
                count = 1
            i+=1
        
        return len(nums)


if(__name__=="__main__"):
    one = Solution()
    print one.removeDuplicates([1,1,1,2,2,3])
