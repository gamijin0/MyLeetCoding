class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.toListWithSeparator(s)

        p = [1]*len(s) #存储以s[i]为中心的回文半径
        p[0]=1
        p[1]=2


        mx=2   # mx = id+p[i]
        id=1

        for i in range(3,len(s)):
            if(mx+id>i):
                p[i] =  min(p[2*id - i],mx-i)








    def toListWithSeparator(self,s:str):
        #将字符串s插入分隔符ch并转化为list
        s = list(s)
        s.sort()
        ch = chr(ord(s[-1])+1)
        res = list()
        for c in s:
            res.append(ch)
            res.append(c)
        res.append(ch)
        return res



a = str("asdfggfdsa")
one = Solution()
print(one.toListWithSeparator(a))