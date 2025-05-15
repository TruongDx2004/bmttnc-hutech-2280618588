# Chương trình tính tổng các số chẵn

# Nhập danh sách các số nguyên, cách nhau bởi dấu phẩy
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))

# Tính tổng các số chẵn
even_sum = sum(number for number in numbers if number % 2 == 0)

# Hiển thị kết quả
print(f"Tổng các số chẵn là: {even_sum}")