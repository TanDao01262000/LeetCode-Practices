class Solution:

    # solution 1: brute force
    #  naive solution is checking all the pair of numbers in the list,
    # to see whether the sum of them equals to the target.


    # solution 2: hashmap  - O(n) time & space complexity
    # converting each value into its index in the array
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # hashmap with in form number:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [i, map[diff]]
            else:
                map[n] = i
        return 