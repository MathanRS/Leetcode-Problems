class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        count = 0
        total = len(nums1) + len(nums2)
        median = total // 2 
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
            else:
                merged.append(nums1[i])
                i += 1

        merged.extend(nums1[i:])  # Appending remaining elements
        merged.extend(nums2[j:])

        if total % 2 == 0:
            return (merged[median] + merged[median - 1]) / 2
        else:
            return merged[median]
