"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""
from typing import List, Tuple
class Solution:
    # Solution 1: using hashmap to group the string with the common hashkey 
    # - O(len(each string in input) * len(input)) time complexity, O(n) space comp 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        res = []
        hashmap = {}

        for st  in strs:
            key = self.hash(st)
            if key not in map:
                map[key] = st
            else:
                temp_val = map[key]
                temp_val.append(str)
                map[key] = temp_val

        for value in map.values():
            res.append(value)
        return res

    def hash(self, st: str) -> Tuple(int):  # O(n) depends on the size of string, O(1) space
        x = tuple()
        for char in st:
            y = x + (ord(char))
            x = y
        return tuple(sorted(x))  # casting into a tuple because we need it to be used as a key in dict

