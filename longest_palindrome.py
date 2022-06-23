class Solution:
    # Solution 1: using hashmap/counter to keep track number of letter
    # add all even, for odd add the even part of it, then add 1 after all if there are odd element in the counter

    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        isOdd = False
        for x in counter.values():
            if x%2 == 0:
                res += x
            else:
                isOdd = True
                res += (x - x%2)
        if isOdd:
            res += 1
        return res
        