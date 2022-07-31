"""Question:
 Design a class to find the kth largest element in a stream. 
 Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    1. KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    2. int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream."""

import heapq
class KthLargest:
    # Solution 1: using min heap 
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # building a heap with heapify() - O(n)

        # pop element which are smaller than the kth biggest element,
        # and now the smallest node in the heap becomes the kth biggest element
        while len(self.min_heap) > self.k: # O(len(min_heap)-k * log n)
            heapq.heappop(self.min_heap) # heappop() - O(log n)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap) # O(log n)
        if len(self.min_heap) > self.k:  
            heapq.heappop(self.min_heap)
        return self.min_heap[0]