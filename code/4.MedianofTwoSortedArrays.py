class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1+= nums2
        nums1.sort()
        if(len(nums1)%2==0):
            return (nums1[int(len(nums1)/2)]+nums1[int(len(nums1)/2-1)]*1.0)/2
        else:
            return nums1[int((len(nums1)+1)/2)-1]



one = Solution
print(one.findMedianSortedArrays(None,[1,3],[2]))