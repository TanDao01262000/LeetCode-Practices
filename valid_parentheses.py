class Solution:
    # Solution 1: using stack -> O(n) space, worst case: O(3n)
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']

        for char in s:
            if (char in close and (len(stack) == 0 or close.index(char) != open.index(stack[-1]))):
                return False
            elif char in close and close.index(char) == open.index(stack[-1]):
                stack.pop(-1)
            elif char in open:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        return False


    # Solution 2: using stack with hashmap, O(3n) time and O(n) space     
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        for char in s:
            if char in hashmap:
                if stack:
                    if hashmap[char] == stack[-1]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False

            else:
                stack.append(char)
        
        if not stack:
            return True
        return False
    
        