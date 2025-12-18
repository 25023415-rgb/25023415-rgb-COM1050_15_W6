danh_sach_cap = input().split()

ket_qua = {}


for cap in danh_sach_cap:
    k, v = cap.split(':')
    
    v = int(v) 

    if k not in ket_qua:
        ket_qua[k] = []
    
    ket_qua[k].append(v)


print(ket_qua)
