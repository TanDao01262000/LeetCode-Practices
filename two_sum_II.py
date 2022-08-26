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


    # Solution 2: using two pointers, left and right
    # similar concept of narrow down the range of the binary search 
    def twoSum(self, numbers: list[int], target:int) -> list[int]:
        res = []
        l, r = 0, len(numbers)
        
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                res.append(l+1)
                res.append(r+1)
                return res