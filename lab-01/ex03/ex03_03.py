# Chương trình tạo Tuple từ danh sách

# Nhập danh sách các phần tử, cách nhau bởi dấu phẩy
elements = input("Nhập danh sách các phần tử, cách nhau bởi dấu phẩy: ").split(',')

# Tạo tuple từ danh sách
result_tuple = tuple(elements)

# Hiển thị tuple
print("Tuple được tạo là:", result_tuple)