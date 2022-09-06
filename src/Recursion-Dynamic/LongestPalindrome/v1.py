class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #Right Idea, sort of working, but the exact way it handlind even vs odd, not quite working
        
        if len(s) == 2:
            if (s[::-1] == s):
                return s
        even = None 
        longest = 0
        palindrome = s[0]
        
        
        def checkPalindromes(l, r, isEven, longest):
            curr = ''
            
            while l >= 0 and r <= len(s) - 1:
                
                if s[l] == s[r]:
                    print(l, r)
                    curr += s[r]
                    print(curr)
                    
                    if len(curr) > longest:
                        longest = len(curr)
                        
                        if isEven:
                            print('even', curr, longest)
                            palindrome = curr[::-1]+curr
                        else:
                            print('odd', curr, longest)
                            palindrome = curr[::-1]+s[i]+curr
                    l -= 1
                    r += 1
                
                else:
                    break
            return palindrome
            
        
        for i in range(1, len(s) - 1):
            print('i', i)
            l = r = - 1
            
            if s[i-1] == s[i+1]:
                l = i - 1
                r = i + 1
                palindrome = checkPalindromes(l, r, False, longest)
                
            if s[i-1] == s[i]:
                l = i -1
                r = i
                palindrome = checkPalindromes(l, r, True, longest)
                
            if s[i+1] == s[i]:
                l = i 
                r = i + 1
                palindrome = checkPalindromes(l, r, True, longest)
                
            
            
        return palindrome