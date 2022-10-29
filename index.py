import time

Start = time.time()
Rarr = [0, 1, 1]

for k in range(3, 100):
    c = Rarr[k-1]*(4*k-10)
    Rarr.append(c)
    print(k, ".", c)

end = time.time()
print("Space: ", len(Rarr), "ints")
print(end-Start, "s")