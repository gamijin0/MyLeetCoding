# coding: utf-8
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if('*' not in p and '.' not in p):
            #若没有通配符
            return (s in p)
        elif('*' not in p):
            #只存在'.'通配符

            if(len(s)>len(p)):
                return False

            j=0
            i=0
            while(i<len(s)):
                if((len(s)-i)>(len(p)-j) or j>=len(p)):
                    return False
                if(p[j]=='.' or p[j]==s[j]):
                    j+=1
                else:
                    j+=1
                i+=1
            return True
        elif('.' not in p):
            #只存在‘*’通配符
            j=0
            tmp=''
            if(p[0]=='*'):
                return False
            i=0
            while(i<len(s)):
                if(j>=len(p)):
                    return False
                if(tmp==s[i]):
                    i+=1
                    continue
                if(p[j]=='*'):
                    if(p[j-1]!='*'):
                        tmp = p[j-1]
                else:
                    tmp = ''

                if(p[j]==s[i] or tmp==s[i]):
                    j+=1
                else:
                    j+=1
                    i-=1

                i+=1

            return True
        else:
            #同时存在'.'和'*'通配符
            i=0
            j=0
            tmp=''
            if(p[0]=='*'):
                return False
            while(i<len(s)):
                if(j>=len(p)):
                    return False
                if(p[j]==s[i]):
                    j+=1
                else:
                    if(p[j]=='.'):
                        j+=1
                    elif(p[j]=='*'):
                        if (p[j - 1] != '*'):
                            tmp = p[j - 1]
                            if(tmp==s[i]):
                                i+=1
                                continue
                        if(p[j-1]=='.'):
                            return True
                    else:
                        tmp=''

                i+=1


one  = Solution()
print (one.isMatch("ab",'.*c'))




















