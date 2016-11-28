class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

    def toListWithSeparator(self,s,ch):
        res = list()
        for c in s:
            res.append(ch)
            res.append(c)
        res.append(ch)
        return res



a = str("asdfggfdsa")
one = Solution()
print(one.toListWithSeparator(a,"#"))