class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        record = set()
        while n not in record:
            record.add(n)
            n = self.cal(n)
            
            if n == 1:
                return True
            
        return False

    def cal(self, n: int) -> int:
            total = 0
            lst = [int(x) for x in str(n)]
            for i in lst:
                total += i**2
            # print(total)
            return total

sol = Solution()
print(sol.isHappy(19))