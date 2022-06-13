# Solution 1: using counter/hashtable number:#appear-times 
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    c = Counter(nums1)
    res = []
    for i in nums2:
        if c[i] > 0:
            res.append(i)
            c[i] -= 1

    return res

# Solution 2: sorting & two pointers
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = j = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i+1, j+1
            else:
                if nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
        return res





nums1 = [4, 9, 5]
nums2 = [9,4,9, 8,4]
print(intersect(nums1, nums2))