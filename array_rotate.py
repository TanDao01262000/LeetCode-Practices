class Solution:
    # Solution 1: pop and insert at the top of the array k times, O(k) time and O(1) space
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums
    
    # Solution 2: rotating the array three times, O(n) time and O(1) space
    def rotate1(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  reverse the entire array
        k = k % len(nums)  # in case k > len(nums)
        i, j = 0, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1 
        
        #  reverse the first k elements
        i, j = 0, k-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1 
          00
        #  reverse the rest of the array
        i, j = k, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1 
        return nums



nums = [2,3,4]
target = 6
sol = Solution()
print(sol.rotate)