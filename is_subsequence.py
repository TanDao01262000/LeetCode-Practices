class Solution:
    # Solution 1: using two pointers on those two s and t strings, and run throughout them - O(n) time complexity and O(1) space
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j  = 0, 0 
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False