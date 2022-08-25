""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. """

from typing import *
class Solution:
    # Solution 1: iteratively find all posible sequence by finding the begin (the element which has no smaller value than it in the set) of the sequence
    # - O(n) time complexity and space 
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set =  set(nums)  # to avoid repeat the process when a begin of a sequence appear more than once
        for num in nums_set:
            max_length = 1
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    max_length += 1
                    num += 1
                res = max(res, max_length)
        return res