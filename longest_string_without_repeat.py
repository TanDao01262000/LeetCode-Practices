class Solution:
    # Solution 1: using sliding windown algo - O(n) time and space 
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        rec = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in rec:
                rec.remove(s[l])
                l += 1
            rec.add(s[i])
            res = max(res, i-l+1)
        return res