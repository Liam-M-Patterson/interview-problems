class Solution:
    def bagOfTokensScore(self, tokens, power):
        
        #sort so we always have access to either the highest or lowest value token availble 
        tokens.sort()
        
        def getScore(l, r, score, power):

            newScore = 0
            #make sure we do not reuse tokens
            if l <= r:

                #try to increase score first if option is allowed, using the lowest power token, to keep as much power as possible
                if tokens[l] <= power:

                    #increase score, and decrease power, shift left pointer
                    newScore = getScore(l+1, r, score +1, power - tokens[l])

                #since we cannot increase the score, try to increase power with highest power token, and see if that allows for a higher score
                elif score >= 1:

                    #decrease score, and increase power, shift right pointer
                    newScore = getScore(l, r-1, score-1, power + tokens[r])
                
            #  we want the max score
            return max(newScore, score)
        
        return getScore(0, len(tokens)-1, 0, power)