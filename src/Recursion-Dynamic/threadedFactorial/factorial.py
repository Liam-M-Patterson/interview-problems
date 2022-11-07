import timeit

start = timeit.default_timer()

def factorial(n):

    if n == 1:
        return n
    
    fact = n*factorial(n-1)
    return fact


res = factorial(400)
stop = timeit.default_timer()

print('Time: ', stop-start)

