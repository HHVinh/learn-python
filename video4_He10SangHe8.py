print("Nhập số thập phân bất kì: ")
so = int(input())

print(f"Số thập phân {so} trong hệ nhị phân là {bin(so)[2:]}")
print("Số thập phân %d trong hệ bát phân là %o" % (so,so))
print(f"Số thập phân {so} trong thập lục phân là {so:X}")

# 1. % formatting
print("Bin: %s" % bin(so)[2:])
print("Oct: %o" % so)
print("Dec: %d" % so)
print("Hex: %x" % so)
print("HEX: %X" % so)

# 2. .format()
print("Bin: {:b}".format(so))
print("Oct: {:o}".format(so))
print("Dec: {:d}".format(so))
print("Hex: {:x}".format(so))
print("HEX: {:X}".format(so))

# 3. f-string
print(f"Bin: {so:b}")
print(f"Oct: {so:o}")
print(f"Dec: {so:d}")
print(f"Hex: {so:x}")
print(f"HEX: {so:X}")
