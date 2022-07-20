class Solution:
    #  Solution 1: using the logic that similiar to fibonaci problem - O(n) time complexity and O(1) space complexity
    def climbStairs(self, n: int) -> int:
        res = [None]*n+1
        if res[n]:
            return res[n]
        if n <= 2:
            return n
        res[n] = res[n-1] + res[n-2]
        return res[n]
        
''' Explanation: 
    Assumption: at step n-th, there is one way to get to it 
                at step (n-1)-th, there is one way to get to n-th step
    Since the answer for this problem at n-th step depends on the answer
    of it with (n-1)th step and (n-2)th step
    --> The logic of fibonaci is applied
'''