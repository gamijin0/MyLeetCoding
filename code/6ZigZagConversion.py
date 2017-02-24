class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows==1):
            return s
        if(numRows==2):
            return s[0::2]+s[1::2]



        res = list()
        s = list(s)

        for i in range(0,numRows):
            res.append([])



        now = 0
        up = False
        for c in s:
            res[now].append(c)
            if(up):
                now -=1
                if(now==-1):
                    now += 2
                    up = False
            else:
                now+=1
                if(now==numRows):
                    now -= 2
                    up = True

        res_str = ""
        for s in res:
            res_str+=''.join(s)

        return res_str


# one =Solution()
# print(one.convert("abc",2))