class Solution:
    # Solution 1: using 2 counter and compare values - O(n) along size of ransomNote dict, O(2n) space complexity
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = collections.Counter(list(magazine))
        r = collections.Counter(list(ransomNote))

        for letter in list(ransomNote):
            if letter not in m or r[letter] > m[letter]:
                return False
        return True

    # Solution 2: using 1 couter and then iterate the magazine to reduce Counter dict, O(n) time complexity to len(magazine)
    #  and O(n) space to the size of ransomNote
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r = collections.Counter(list(ransomNote))
        
        for i in list(magazine):
            if i in r:
                r[i] -= 1
        for x in r.values():
            if x > 0:
                return False
        return True