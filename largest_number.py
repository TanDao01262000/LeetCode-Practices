# https://leetcode.com/problems/largest-number/

"""Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: '9534330' """

''' Solution 1: Sorting the array by checking the combianation of each pair of number,
    if ab > ba so a should be placed in front of b or a is a larger significant number.

    Apply sorted() with cmp_to_key()
    --> Time complexity = O(nlogn)
        Space complexity = O(1)
'''  

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def cmp(a, b):
            pass

        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int(''.join(nums)))     # THIS IS TO AVOID THE CASE OF [0, 0, 0, 0, 0, 0,......] (ALL ZERO IN THE ARRAY)



