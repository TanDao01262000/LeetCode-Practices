# Solution 1: using set - O(n) time and space complexity, due to set()
def containduplicate(self, nums: List[int]) -> bool:
    if len(set(nums)) != len(nums):
        return True
    return False


# Solution 2: using hashset - O(n) time and space, due to loop and map
def containduplicate1(self, nums: List[int]) -> bool:
    hashset = set()  # set
    for n in nums:
        if n in hashset:
            return True 
        else:
            hashset.add(n)
    return False

# Solution 3: using hashmap - O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        map ={}
        for n in nums:
            if n in map:
                return True
            else:
                map[n] =n