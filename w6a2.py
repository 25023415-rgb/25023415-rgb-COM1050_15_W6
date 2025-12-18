nums = list(map(int, input().split()))

ket_qua = []
tong_tam_thoi = 0

for so in nums:
    tong_tam_thoi += so
    ket_qua.append(tong_tam_thoi)

print(ket_qua)