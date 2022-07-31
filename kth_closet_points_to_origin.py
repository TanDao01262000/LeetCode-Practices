from re import S
from typing import List
from math import sqrt
import heapq
 
class Solution:
    # Solution 1: using heap, dict - O(k log n ) time complexity and O(3n) space complexity
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(self, point: list[int]) -> float: # - O(1)
            return sqrt(point[0] ** 2 + point[1] ** 2)
        dis = []
        dct = {}
        res = []
        for point in points: # - O(n) time complexity 
            dist = distance(point)
            dis.append(dist)
            if dist not in dct:
                dct[dist] = [(point[0], point[1])]
            else:
                temp = dct[dist]
                temp.append((point[0], point[1]))
                dct[dist] = temp

        heapq.heapify(dis) # linear time complexity
        for _ in range(k): # - O(k log n)
            temp = []
            val = heapq.heappop(dis)
            obj = dct.get(val).pop(0)
            temp.append(obj[0])
            temp.append(obj[1])
            res.append(temp)

        return res

    