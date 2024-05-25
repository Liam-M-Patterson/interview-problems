class Solution:
    def wordBreak(self, s: str, wordDict):
        combos = []
        def dfs(l, r, res):
            while r <= len(s):
                word = s[l:r]
                
                if word in wordDict:
                    newRes = res.copy()
                    newRes.append(word)
                    
                    if r == len(s):
                        combos.append(newRes)
                        
                    dfs(r, r+1, newRes)
                r += 1
            return res
        dfs(0, 0, [])
        res = [" ".join(combo) for combo in combos]
        return res
        