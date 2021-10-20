

input = []
a = []

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
Output = 3

input.append([nums1, nums2])
a.append(Output)

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
Output = 5

input.append([nums1, nums2])
a.append(Output)

class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
