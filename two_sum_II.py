class Solution:
    #  Solution 1: using hashmap -O(n) time and space
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        res = []
        idx = 1
        hmap = dict()
        for num in numbers:
            if len(res) < 2:
                if target-num in hmap:
                    res.append(hmap.get(target-num))
                    res.append(idx)
                    
                else:
                    hmap[num] = idx
                idx += 1
            else:
                break
        return res