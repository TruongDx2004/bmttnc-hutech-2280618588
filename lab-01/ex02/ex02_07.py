# Nhập vào nhiều dòng và chuyển thành in hoa

print("Nhập vào các dòng (nhấn Enter trên dòng trống để kết thúc):")

# Nhập nhiều dòng từ người dùng
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Chuyển từng dòng thành in hoa
uppercase_lines = [line.upper() for line in lines]

# Hiển thị các dòng in hoa
print("Các dòng in hoa:")
for line in uppercase_lines:
    print(line)