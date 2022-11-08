class Solution:
    def makeGood(self, s: str) -> str:
        
        # start at second character, so we compare the current char to previous
        for i in range(1, len(s)):
        
            # 32 is the difference in ASCII values for the same captial and lowercase letter, i.e. 'a' and 'A'

            # check if previous was capital
            if ord(s[i]) == ord(s[i-1]) + 32:
                # recursively call makeGood function, with the "bad characters" removed
                return self.makeGood(s[0:i-1]+s[i+1:])

            # check if previous was lowercase
            if ord(s[i]) == ord(s[i-1]) - 32:
                return self.makeGood(s[0:i-1]+s[i+1:])

        # if no "bad characters" found, then the string is good, return that
        return s                