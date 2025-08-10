so = input("Nhập số nguyên hệ 10: ")
isFlag = 0

try:
    so = int(so)
    isFlag = 1
except:
    print("Dữ liệu đầu vào không hợp lệ")

if isFlag:
    print(f"Số {so} hệ 10 chuyển sang hệ 2 là: {bin(so)[2:]}")
    print(f"Số {so} hệ 10 chuyển sang hệ 8 là: {so:o}")
    print(f"Số {so} hệ 10 chuyển sang hệ 16 là: {so:X}")