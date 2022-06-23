class Solution:
    def leftmost_binary_search(self, nums: list[int], target) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l


nums = [1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8]
sol = Solution()
print(sol.leftmost_binary_search(nums, 6))
