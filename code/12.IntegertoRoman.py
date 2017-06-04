class Solution(object):
    def get_str_for_singal(self,num, child, father, grandpa):
        if(num=='0'):
            return ""
        if (num == '1'):
            return child
        if (num == '2'):
            return child + child
        if (num == '3'):
            return child + child + child
        if (num == '4'):
            return child + father
        if (num == '5'):
            return father
        if (num == '6'):
            return father + child
        if (num == '7'):
            return father + child + child
        if (num == '8'):
            return father + child + child + child
        if (num == '9'):
            return child + grandpa

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tmp = ""
        val_str = str(num)


        if (len(val_str) == 4):
            tmp = self.get_str_for_singal(num=val_str[0], child="M", father="", grandpa="")
            return tmp + self.intToRoman( int(val_str[1:]))
        if (len(val_str) == 3):
            tmp = self.get_str_for_singal(num=val_str[0], child="C", father="D", grandpa="M")
            return tmp + self.intToRoman( int(val_str[1:]))
        if (len(val_str) == 2):
            tmp = self.get_str_for_singal(num=val_str[0], child="X", father="L", grandpa="C")
            return tmp + self.intToRoman( int(val_str[1:]))
        if (len(val_str) == 1):
            tmp = self.get_str_for_singal(num=val_str[0], child="I", father="V", grandpa="X")
            return tmp

if(__name__=="__main__"):
    one = Solution()
    for i in range(1,3999):
        print(i,one.intToRoman(i))