tup = tuple(map(int, input().split()))

k = int(input())

n = len(tup)
if n > 0:
    k = k % n 
    
    ket_qua = tup[k:] + tup[:k]
else:
    ket_qua = tup

print(ket_qua)