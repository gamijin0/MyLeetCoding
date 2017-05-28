class Solution(object):

    def findDuplicates(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        if(len(nums)==0 or len(nums)==1):

            return []

        

        self.res = []

        self.nums = nums

        front = 0

        back = len(nums)-1

        while(True):

            v = nums[front]-1

            if(front==v):

                front+=1

                continue

            if(self.swap(front,v)==1):

                pass

            else:

                if(back>front):

                    self.swap(front,back)

                    print "back:",back
                    back-=1

                else:

                    break

        return self.res

    

    def swap(self,f,b):

        print f,b
        if(self.nums[f]==self.nums[b]):

            self.res.append(self.nums[f])

            print "#"
            return 0

        else:
            temp = self.nums[f]

            self.nums[f] = self.nums[b]

            self.nums[b] =temp

            return 1

        

        
if(__name__=="__main__"):
    one = Solution()
    print one.findDuplicates([4,3,2,7,8,2,3,1])
        

        

        
