class Solution(object):

    top = ""
    separator = ""

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.toListWithSeparator(s)

        p = [1]*len(s) #存储以s[i]为中心的回文半径
        p[0]=1
        p[1]=10
        p[2]=2


        mx=2   # mx = id+p[i]
        id=1

        for i in range(3,len(s)):
            if(mx>i):
                p[i] =  min(p[2*id - i],mx-i)
            else:
                p[i]=1
            while(i+p[i]<len(s) and s[i+p[i]]==s[i-p[i]] ):
                p[i]+=1
            if(i+p[i]>mx):
                mx = i +p[i]
                id = i

        resid = p.index(max(p))
        res = s[resid-p[resid]+1:resid+p[resid]-1]

        for i in range(len(res)-1,-1,-1):
            if(res[i]==self.separator):
                res.pop(i)
        return ''.join(res)


    def toListWithSeparator(self,st):
        #将字符串s插入分隔符ch并转化为list
        s = list(st)
        tmp = list(st)
        tmp.sort()
        ch = chr(ord(tmp[-1])+1)
        top = chr(ord(ch)+1)
        self.separator = ch
        self.top = top
        res = list()
        res.append(top)
        for c in s:
            res.append(ch)
            res.append(c)
        res.append(ch)
        return res

# a = "asdfdsa"
# one = Solution()
# print(one.longestPalindrome(a))