# Chương trình nhập danh sách các số, đảo ngược danh sách và in ra dạng [0, 1, 2]

# Nhập danh sách các số, cách nhau bởi dấu phẩy
numbers = list(map(int, input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ").split(',')))

# Đảo ngược danh sách
reversed_numbers = numbers[::-1]

# Hiển thị danh sách đã đảo ngược
print("Danh sách sau khi đảo ngược:", reversed_numbers)