class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        sumArray = list()
        x = len(nums1)
        y = len(nums2)
        while i < x and j < y:
            if nums1[i] < nums2[j]:
                sumArray.append(nums1[i])
                i += 1
            else:
                sumArray.append(nums2[j])
                j += 1
        sumArray.extend(nums2[j:]) if i == x else sumArray.extend(nums1[i:])
        l = len(sumArray)
        if l % 2 == 1:
            result = sumArray[l//2]
        else:
            result = (sumArray[l//2]+sumArray[(l//2-1)])/2
        return result