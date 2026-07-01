import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Cấu hình trang Streamlit
st.set_page_config(page_title="Linear Algebra Visualizer", layout="wide")

st.title("Linear Algebra Visualizer")
st.subheader("Giai đoạn 1: Ma trận như một phép biến đổi không gian")

# --- Sidebar: nhập ma trận ---
st.sidebar.header("Nhập ma trận 2x2")
a = st.sidebar.number_input("a11", value=1.0, step=0.5)
b = st.sidebar.number_input("a12", value=0.0, step=0.5)
c = st.sidebar.number_input("a21", value=0.0, step=0.5)
d = st.sidebar.number_input("a22", value=1.0, step=0.5)

A = np.array([[a, b], [c, d]])
st.sidebar.write("Ma trận A:")
st.sidebar.write(A)

# --- Hình vuông đơn vị (4 góc) ---
# Tọa độ các điểm: (0,0), (1,0), (1,1), (0,1), và quay về (0,0) để khép kín hình
unit_square = np.array([
    [0, 0], [1, 0], [1, 1], [0, 1], [0, 0]
]).T  # Dùng .T để chuyển vị thành shape (2, 5)

# Nhân ma trận A với các điểm của hình vuông để tạo ra hình biến đổi
transformed_square = A @ unit_square

# --- Hai vector cơ sở ---
e1 = np.array([1, 0])
e2 = np.array([0, 1])
e1_new = A @ e1
e2_new = A @ e2

# --- Vẽ biểu đồ bằng Matplotlib ---
fig, ax = plt.subplots(figsize=(6, 6))

# Hình vuông gốc (xám, nét đứt)
ax.plot(unit_square[0], unit_square[1], "--", color="gray", label="Không gian gốc")

# Hình vuông sau biến đổi (xanh, nét liền)
ax.plot(transformed_square[0], transformed_square[1], "-", color="royalblue", linewidth=2, label="Sau biến đổi")
# Tô màu vùng không gian bị biến đổi
ax.fill(transformed_square[0], transformed_square[1], color="royalblue", alpha=0.2)

# Vector cơ sở gốc (xám)
ax.quiver(0, 0, e1[0], e1[1], angles="xy", scale_units="xy", scale=1, color="gray", width=0.008)
ax.quiver(0, 0, e2[0], e2[1], angles="xy", scale_units="xy", scale=1, color="gray", width=0.008)

# Vector cơ sở sau biến đổi (đỏ và cam)
ax.quiver(0, 0, e1_new[0], e1_new[1], angles="xy", scale_units="xy", scale=1, color="crimson", width=0.012, label="A·e1")
ax.quiver(0, 0, e2_new[0], e2_new[1], angles="xy", scale_units="xy", scale=1, color="darkorange", width=0.012, label="A·e2")

# Thiết lập giới hạn trục tọa độ linh hoạt dựa trên kích thước hình biến đổi
lim = max(3, np.abs(transformed_square).max() + 1)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

# Vẽ trục x=0 và y=0
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

ax.set_aspect("equal") # Giữ tỉ lệ 1:1 cho trục x và y
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left")

# Hiển thị biểu đồ lên Streamlit
st.pyplot(fig)

# --- Thông tin số học ---
col1, col2 = st.columns(2)
with col1:
    st.metric("Định thức (det A)", f"{np.linalg.det(A):.3f}")
    # Đã hoàn thiện câu caption bị thiếu
    st.caption("det A = tỉ lệ thay đổi diện tích. Âm nghĩa là không gian bị lật ngược.")

with col2:
    st.metric("Hạng ma trận (rank)", np.linalg.matrix_rank(A))
    # Đã hoàn thiện câu caption bị thiếu
    st.caption("Rank < 2 nghĩa là không gian bị nén thành 1 đường thẳng hoặc 1 điểm.")