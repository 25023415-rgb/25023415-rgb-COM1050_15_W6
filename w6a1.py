n = list(map(int, input().split()))
danhsach = []
for i in n:
    if i not in danhsach:
        danhsach.append(i)
print(danhsach)
