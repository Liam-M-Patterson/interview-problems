class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}

        # depth first search recursive function
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            # can always add single character, if its not zero
            res = dfs(i+1)
            # if the string continues beyond the next character
            # and the next number is 1X or 2[0123456]
            if (i+1<len(s) and (s[i] == '1' or 
                (s[i] == '2' and s[i+1] in "0123456"))):
                res += dfs(i+2)
            
            dp[i] = res
            return res
        
        return dfs(0)
