# Nhập vào các số nhị phân 4 chữ số, kiểm tra xem có chia hết cho 5 không và in ra các số đó

# Nhập vào các số nhị phân, cách nhau bởi dấu phẩy
binary_numbers = input("Nhập vào các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ").split(',')

# Lọc các số chia hết cho 5
divisible_by_5 = []
for binary in binary_numbers:
    if len(binary) == 4 and all(char in '01' for char in binary):  # Kiểm tra số nhị phân hợp lệ
        decimal_value = int(binary, 2)  # Chuyển nhị phân sang thập phân
        if decimal_value % 5 == 0:
            divisible_by_5.append(binary)

# Hiển thị các số nhị phân chia hết cho 5
print("Các số nhị phân chia hết cho 5 là:", ", ".join(divisible_by_5))