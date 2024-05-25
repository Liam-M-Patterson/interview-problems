import time
numIters = 1000000
print("String concatenation:")
ts = time.time()
s = ""
for i in range(numIters):
    s += str(i) + ","

s1 = s
print(time.time() - ts)

print("List append and join on comma")
ts = time.time()
s = []
for i in range(numIters):
    s.append(str(i))

s2 = ",".join(s)
print(time.time() - ts)

print("List append twice and join on nothing")
ts = time.time()
s = []
for i in range(numIters):
    s.append(str(i))
    s.append(",")

s3 = "".join(s)
print(time.time() - ts)

print("List append once with concate string and join on nothing")
ts = time.time()
s = []
for i in range(numIters):
    s.append(str(i) + ",")
    

s4 = "".join(s)
print(time.time() - ts)

print(len(s1))
print(len(s2))
print(len(s3))
print(len(s4))
# print(s1 == s2 == s3 == s4)