class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1):
            return len(s)
        res = 0
        i=0
        j=1
        while(j<len(s)):
            if(s[j] not in s[i:j]):
                if(j-i+1>res):
                    res = j-i+1
            else:
                i+=1
                j-=1
            j+=1
        return res

