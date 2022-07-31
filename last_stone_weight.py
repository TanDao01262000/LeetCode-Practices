import heapq
class Solution:
    # Solution 1: using loop and array slice, O( n^2 log n) run time and O(1) space complexity
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 0:
            return 0 
        if len(stones) == 1:
            return stones[0]
        stones.sort()  # O(n log n) for tim sort
        while len(stones) > 1:
            if stones[-1] > stones[-2] or stones[-1] < stones[-2]:
                stones[-2] = abs(stones[-1] - stones[-2])
                stones= stones[:-1]
                stones.sort()
            elif stones[-1] == stones[-2]:
                stones = stones[:-2]
        stones.append(0)
        return stones[0]
    
    # Solution 2: using heap, O((n-1) log n) time complexity and O(1) space complexity
    def lastStonesWeight1(self, stones: list[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)
            if f < s:
                heapq.heappush(stones, f-s)
        stones.append(0)
        return stones[0]        