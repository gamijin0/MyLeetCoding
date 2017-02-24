class Solution(object):
    def get_num_from_char(self, ch):
        if (ch == 'I'):
            return 1
        if (ch == 'V'):
            return 5
        if (ch == 'X'):
            return 10
        if (ch == 'L'):
            return 50
        if (ch == 'C'):
            return 100
        if (ch == 'D'):
            return 500
        if (ch == 'M'):
            return 1000

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==1):
            return self.get_num_from_char(s)
        else:
            a = self.get_num_from_char(s[0])
            b = self.get_num_from_char(s[1])
            if(a>=b):
                return a + self.romanToInt(s[1:])
            else:
                return self.romanToInt(s[1:]) - a

if(__name__=="__main__"):
    one = Solution()
    print 3998,one.romanToInt("MMMCMXCVIII")