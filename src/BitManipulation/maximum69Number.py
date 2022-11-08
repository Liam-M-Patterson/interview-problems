class Solution:
    def maximum69Number (self, num: int) -> int:
        
        digit_position = 0
        highest_six = -1
        num_copy = num
        
        # Check every digit of 'num_copy' from low to high.
        while num_copy:
            # If the current digit is '6', record it as the highest digit of 6.
            if num_copy % 10 == 6:
                highest_six = digit_position
            
            # Move on to the next digit.
            num_copy //= 10
            digit_position += 1
        
        # If we don't find any digit of '6', return the original number,
        # otherwise, increment 'num' by the difference made by the first '6'.
        return num if highest_six == -1 else num + 3 * 10 ** highest_six