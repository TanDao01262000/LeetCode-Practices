class Solution:
    # Solution: Bit manipulation "^" - XOR function
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res = i ^ res
        return res

''' Feature: n ^ 0/ n XOR 0 = n
    Since there are duplicates in the list
    The result of "^" all the element with duplicate is 0
    Therefore, the final result will be the finding element XOR with 0
    or just the element we are finding
    '''
