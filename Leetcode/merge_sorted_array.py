# Solution 1: merging 2 sorted arrays, 0(m+n) time and O(m) space
from tkinter import N


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        arr1 = nums1[:m]

        while i < m and j < n:
            if arr1[i] < nums2[j]:
                nums1[k] = arr1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < n:
            nums1[k] = arr1[i]
            i += 1
            k += 1

        while j < m:
            nums1[k] = nums2[j]
            j += 1
            k += 1

        return None


# Solution 2 (better one): O(m+n) time and O(1) space
def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

     k = len(nums1) - 1

     while i > 0 and j > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[k] = nums1[m-1]
            m -= 1
        else:
            nums1[k] = nums2[n-1]
            n -= 1
        k -= 1

    while n > 0:
        nums1[k] = nums2[n-1]
        n, k = n-1, k-1