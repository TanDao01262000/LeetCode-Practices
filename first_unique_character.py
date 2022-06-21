
class Solution:
    # Solution 1: using hashmap to store the index of
    #  the letter in the string if it is not duplicated, otherwise -1 
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        i = 0
        for letter in list(s):
            if letter in hashmap:
                hashmap[letter] = -1
            else:
                hashmap[letter] = i
            i += 1
            
        for value in hashmap.values():
            if value != -1:
                return value
            
        return -1

    # Solution 2: using counter
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(list(s))
        
        for i in range(len(s)):
            if c.get(s[i]) == 1:
                return i
        return -1 