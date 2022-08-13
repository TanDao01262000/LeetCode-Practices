"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""
from typing import *
class Solution:
    #  Solution 1: finding prefix and postfix product of a number and using the result array to save 
    # - O(n) time complexity and O(1) space complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1   # the first value of both pre and post fix is 1, since no number after last element and no number before first element
        res = [prefix] # res is used as place to store prefix product, begins with 1

        # prefix compute and store
        for i in range(len(nums)-1):  # O(n) time complexity
            prefix *= nums[i]
            res.append(prefix)

        # finish by multiply prefix by postfix
        for j in range(len(nums)-1,-1, -1):   # O(n) time complexity
            res[j] *= postfix
            postfix *= nums[j]

        return (res)

