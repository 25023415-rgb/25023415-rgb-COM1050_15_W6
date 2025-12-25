n = list(tuple(int(x) for x in input().split()))
sochan = []
sole = []
for i in n:
    if i % 2 == 0:
        sochan.append(i)
    else:
        sole.append(i)