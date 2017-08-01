#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard
#
# algorithms
# Medium (38.92%)
# Total Accepted:    2.3K
# Total Submissions: 5.8K
# Testcase Example:  '3'
#
# 
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step: 
# 
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# 
# 
# 
# 
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'. 
# 
# 
# Example 1:
# 
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# 
# 
# 
# 
# Note:
# 
# The n will be in the range [1, 1000].
# 
# 
#
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1):
            return 0
        if(n in [2,3,5,7,11]):
            return n

        x  = int(n/2)
        while(x>=1):
            if(n%x==0):
                break
            else:
                x-=1

        if(x==1):
            return n
        else:
            basic = self.minSteps(x)
            return basic+int(n/x)


if(__name__=="__main__"):
    one = Solution()
    print(one.minSteps(9))


