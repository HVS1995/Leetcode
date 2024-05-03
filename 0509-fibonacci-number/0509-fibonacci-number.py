class Solution:
    def fib(self, n: int) -> int:
        dp = [None]*(n+1)
        def fb(n):
            if dp[n]!= None:
                return dp[n]
            if n== 0 or n==1:
                dp[n] = n
            else:
                dp[n] = fb(n-1)+fb(n-2)
                
            return dp[n]
        return fb(n)
        