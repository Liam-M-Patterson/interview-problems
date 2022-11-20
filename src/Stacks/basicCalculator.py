# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 
# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

class Solution:

    def calculate(self, s: str) -> int:
        def isDigit(ch):
            return ord(ch) >= ord('0') and ord(ch) <= ord('9')

        r = 0
        sum = 0
        sign = 1
        stack = []
        
        while r < len(s):
            
            ch = s[r]
            
            if isDigit(ch):
                l = r
                # check for multi digit numbers
                while r +1 < len(s) and isDigit(s[r+1]):
                    r += 1

                sum += sign * int(s[l:r+1])
                
            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1

            elif ch == '(':
                # save the sum and sign into a stack
                stack.append(sum)
                stack.append(sign)
                # reset the sum and sign, since we are inside brackets
                sum = 0
                sign = 1

            elif ch == ')':
                sum = sum * stack.pop() + stack.pop()
                sign = 1

            r += 1
        return sum