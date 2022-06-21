
class Solution:
    # using one pointer to keep track the left sum of at an index -> O(n) time complexity and O(1) space
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for idx in range(len(nums)):
            if left_sum == total - left_sum - nums[idx]:
                return idx
            left_sum += nums[idx]
        return -1

