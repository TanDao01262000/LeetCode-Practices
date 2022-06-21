class Solution:
    # Solution 1: using 2 counter and comapre, O(n) time and space
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(sorted(list(s))) == collections.Counter(sorted(list(t)))

    # Solution 2: using count() to check the frequency of letter in strings,  O(n) time O(1) space

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for each in set(s):
            if s.count(each) != t.count(each):
                return False
        else:
            return True

    # Solution 3: manually count, O(n)  space and time
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS.keys():
            if countS[c] != countT.get(c, 0):
                return False
        return True

    # Solution 4: Sorting - O(n^2)/O(nlogn) time and O(1) time
    def isAnagram(self, s: str, t: str) -> bool:
        return sort(s) == sort(t)
