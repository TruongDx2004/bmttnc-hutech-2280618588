# Xây dựng mảng 2 chiều với a[i][j] = i * j

# Nhập giá trị x và y
x = int(input("Nhập số hàng (x): "))
y = int(input("Nhập số cột (y): "))

# Tạo mảng 2 chiều
array = [[i * j for j in range(y)] for i in range(x)]

# Hiển thị mảng 2 chiều
print("Mảng 2 chiều:")
for row in array:
    print(row)