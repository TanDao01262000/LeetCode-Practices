class Solution:
    # Solution 1: using array to save the max_sum of the left value(s) / semi-dynamic - O(n) time and space
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        list = [0] * len(nums)
        list[0] = nums[0]
        for n in range(1, len(nums)):
            if nums[n] > list[n-1] + nums[n]:
                list[n] = nums[n]
                if nums[n] > max_sum:
                    max_sum = nums[n]
            else:
                list[n] = list[n-1] + nums[n]

                if list[n-1] + nums[n] > max_sum:
                    max_sum = list[n-1] + nums[n]

        return max_sum

        # Solution 2: Sliding windown, O(n) time and O(1) for space

    def maxSubArray1(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:  # get rid of all the negative prefix sum -> sliding windown
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)

        return max_sum
