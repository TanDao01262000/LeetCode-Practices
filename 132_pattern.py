# Solution 1: using stack and monotonic decreasing order
def find123pattern(self, nums: List[int]) -> bool:
    stack = [] # contains a pair of value, one is the biggest value and a smallest value right before the first number, [val, min]
    cur_min = nums[0]

    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True

        stack.append([n, cur_min])
        cur_min = min(n, cur_min)
    
    return Falsex