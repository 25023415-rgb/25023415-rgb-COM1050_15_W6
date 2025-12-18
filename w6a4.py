# 1. Nhập và tách chuỗi
danh_sach_cap = input().split()

# 2. Khởi tạo dictionary rỗng
ket_qua = {}

# 3. Duyệt qua từng cặp
for cap in danh_sach_cap:
    # 4. Tách key và value
    k, v = cap.split(':')
    
    # 5. Chuyển value thành số
    v = int(v) 

    # 6. Kiểm tra sự tồn tại của key
    if k not in ket_qua:
        ket_qua[k] = []
    
    # 7. Thêm value vào list
    ket_qua[k].append(v)

# 8. In kết quả
print(ket_qua)