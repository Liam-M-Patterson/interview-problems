# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

# Example 1:
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45

# Example 2:
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:        

        def computeOverlapArea():
            
            # since we know that a1 is always <= than a2, and likewise for b
            # we can be sure that the lower y coordinate will be the maximum of ay1 and by1
            # and the upper coordinate will be the minimum of ay2 and by2
            Y1 = max(ay1, by1)
            Y2 = min(ay2, by2)

            # same logic that applies for the y coords applies to the x coords
            X1 = max(ax1, bx1)
            X2 = min(ax2, bx2)

            # the above calculations didn't actually consider whether or not the points overlapped
            # just found the rectangle that exists between the extreme ends of the points. 
            # now need to check to make sure the rectangles actually overlap, and compute that area
            if Y1 < Y2 and X1 < X2:
                return (Y2 - Y1) * (X2 - X1)
            return 0

        overlap = computeOverlapArea()
        area1 = (ay2-ay1) * (ax2-ax1)
        area2 = (by2-by1) * (bx2-bx1) 
        return (area1 + area2 - overlap)
                
