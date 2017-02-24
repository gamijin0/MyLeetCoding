class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):
            return ""
        for s in strs:
            if(len(s)==0):
                return ""

        flag = True
        num_of_common = 0
        while(flag):
            num_of_common += 1
            if(num_of_common-1 == len(strs[0])):
                num_of_common -= 1
                flag = False
                break
            else:
                tmp_ch = strs[0][num_of_common-1]
            for s in strs:
                if (num_of_common - 1 == len(s)):
                    num_of_common -= 1
                    flag = False
                    break
                else:
                    if(s[num_of_common-1]!=tmp_ch):
                        num_of_common -= 1
                        flag = False
                        break

        return strs[0][0:num_of_common]

if(__name__=="__main__"):
    one = Solution()
    print one.longestCommonPrefix(["a"])
    print one.longestCommonPrefix(["a","a"])
    print one.longestCommonPrefix(["c123","c22"])