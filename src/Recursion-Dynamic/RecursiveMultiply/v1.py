import sys

def minProduct(a: int, b: int):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    
    # divide by 2
    s = smaller >> 1
    halfProd = minProductHelper(s, bigger)
    
    if (smaller % 2 == 0):
        return (halfProd+halfProd)
    else:
        return (halfProd + halfProd + bigger)

if __name__ == "__main__":
    
    res = minProduct(3, 5)
    print(res)
    # print(res.getAnswer())