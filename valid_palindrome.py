"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution:
    # Solution 1: using two pointer method - O(n) time and space complexity
    def isPalindrome(self, s: str) -> bool:
        lst = s.lower()
        lst1 = []
        for char in lst:
            if  char.isnumeric() or char.isalpha():
                lst1.append(char)
        i, j = 0, len(lst1)-1
        while i < j:
            if lst1[i] != lst1[j]:
                return False
            i, j = i+1, j-1
        return True