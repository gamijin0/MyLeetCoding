class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0

        tmp =str(x)
        if(x<0):
            res = int(tmp[0]+tmp[1:][::-1])
            return  res if(res>=-2147483647) else 0
        else:
            res = int(tmp[::-1])
            return res if(res<=2147483647) else 0
