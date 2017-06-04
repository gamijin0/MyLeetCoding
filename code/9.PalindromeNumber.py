class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        if (x > 2147483647 or x < -2147483647):
            return False

        if (str(x) == str(x)[::-1]):
            return True
        else:
            return False