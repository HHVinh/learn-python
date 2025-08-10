# Exercise 1: Graph Representation - Adjacency Matrix
# Implement a graph data structure using an adjacency matrix
# representation. The adjacency matrix is a 2D array where each cell
# 𝐴 𝑖 [𝑗] represents the weight of the edge from vertex 𝑖 to vertex 𝑗 . If no
# edge exists, the value is 0.

# Bài tập 1: Biểu diễn đồ thị – Ma trận kề
# Cài đặt cấu trúc dữ liệu đồ thị sử dụng cách biểu diễn ma trận kề.
# Ma trận kề là một mảng 2 chiều, trong đó mỗi ô A[i][j] biểu thị trọng số của cạnh từ đỉnh i đến đỉnh j.
# Nếu không tồn tại cạnh, giá trị tại ô đó là 0.


class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.ma_tran_ke = [[0] * so_dinh for _ in range(so_dinh)]

    def them_canh(self, dinh_dau, dinh_cuoi, trong_so):
        """Thêm cạnh vào ma trận kề"""
        self.ma_tran_ke[dinh_dau][dinh_cuoi] = trong_so

    def ton_tai_canh(self, dinh_dau, dinh_cuoi):
        """Kiểm tra cạnh đã tồn tại chưa"""
        return self.ma_tran_ke[dinh_dau][dinh_cuoi] != 0

    def in_ma_tran(self):
        """In ma trận kề"""
        for hang in self.ma_tran_ke:
            print(hang)


if __name__ == "__main__":
    # Nhập số đỉnh
    while True:
        try:
            so_dinh = int(input("Nhập số đỉnh của đồ thị: "))
            if so_dinh > 0:
                break
            else:
                print("Số đỉnh phải lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")

    do_thi = DoThi(so_dinh)

    # Nhập số cạnh
    while True:
        try:
            so_canh = int(input("Nhập số cạnh của đồ thị: "))
            if 0 <= so_canh <= so_dinh * so_dinh:
                break
            else:
                print("Số cạnh không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")

    # Nhập thông tin từng cạnh
    canh_da_nhap = 0
    while canh_da_nhap < so_canh:
        try:
            print(f"\nNhập thông tin cho cạnh thứ {canh_da_nhap + 1}:")
            dinh_dau = int(input("  Đỉnh xuất phát (0 đến {}): ".format(so_dinh - 1)))
            dinh_cuoi = int(input("  Đỉnh kết thúc (0 đến {}): ".format(so_dinh - 1)))
            trong_so = int(input("  Trọng số của cạnh: "))

            # Kiểm tra phạm vi đỉnh
            if not (0 <= dinh_dau < so_dinh and 0 <= dinh_cuoi < so_dinh):
                print("❌ Lỗi: Đỉnh ngoài phạm vi, vui lòng nhập lại.")
                continue

            # Kiểm tra trùng cạnh
            if do_thi.ton_tai_canh(dinh_dau, dinh_cuoi):
                print("❌ Lỗi: Cạnh này đã tồn tại, vui lòng nhập lại.")
                continue

            # Thêm cạnh
            do_thi.them_canh(dinh_dau, dinh_cuoi, trong_so)
            canh_da_nhap += 1

        except ValueError:
            print("❌ Lỗi: Vui lòng nhập số nguyên hợp lệ.")

    # In kết quả
    print("\nMa trận kề của đồ thị là:")
    do_thi.in_ma_tran()
