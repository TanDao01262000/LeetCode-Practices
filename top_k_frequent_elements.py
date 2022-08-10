# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# time complexity must not bigger than a*log a
class Solution:
    # Solution 1: using hashmap and sorting hashmap method, assume size of input is a, # distinguish key in the dict is b
    # - O(b log b) time complexity, O(a+b) space complexity, Since a <= b, therefore the condition is still being satisfied
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        freq = {}
        for num in nums:  # O(a) run time, the most taken run time in the program
            freq[num] = freq.get(num, 0) + 1
        res = []
        new_freq = dict(sorted(freq.items(), key=lambda s: s[1], reverse=True))  # O(b log b) time complexity
        keys_list = list(new_freq.keys())
        for i in range(k):
            res.append(keys_list[i])
        return res

    # Solution 2: using hashmap to count, then utilize the index in an array to gather all number with the same frequency,
    #  then loop through from the back of the array to get k element.
    #  - O(n) time compelexity since the # elements + # frequency is fixed. 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            counter[i] = counter.get(i, 0) +1  # O(n) runtime
        for key, count in counter.items():
            freq[count].append(key)
        
        res = []
        for i in range(len(freq)-1, 0, -1):  # O(n) runtime
            for n in freq[i]:
                if len(res) == k:
                    break
                res.append(n)

        return res




