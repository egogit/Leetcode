# Use Greedy Algorithm

class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0;
        
        for k in range(2,n+1):
            s = n // k;  # s candies for k-r people
            r = n % k;   # s+1 candies for r people
            result = ((s+1)**r)*(s**(k-r));
            if result >= ans:
                ans = result
            else:
                break;
        
        return ans