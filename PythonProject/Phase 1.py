import numpy as np

# 1. Khai báo Vector v có tọa độ (3, -2)
v = np.array([3, -2])

# 2. Khai báo Ma trận xoay 90 độ (A)
# [0  -1]
# [1   0]
A = np.array([
    [0, -1],
    [1,  0]
])

# 3. Thực hiện phép biến đổi (Nhân ma trận A với vector v)
# Trong NumPy, chúng ta dùng dot() hoặc toán tử @
v_new = A.dot(v)
# hoặc v_new = A @ v

print("Tọa độ mới của vector là:", v_new)
# Kết quả sẽ in ra: [2, 3]