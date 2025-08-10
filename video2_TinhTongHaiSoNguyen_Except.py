try:
    print("Nhập số thứ 1:")
    so1 = int(input())
    print("Nhập số thứ 2:")
    so2 = int(input())

    tong = so1 + so2

    print(f"Tổng {so1} + {so2} = {tong}")
except:
    print("Lỗi nhập dữ liệu không hợp lệ")