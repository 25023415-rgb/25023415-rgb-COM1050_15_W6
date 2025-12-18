danh_sach = input().split()

demsolan = {}

for tu in danh_sach:
    if tu in demsolan:
        demsolan[tu] += 1
    else:
        demsolan[tu] = 1


print(demsolan)
