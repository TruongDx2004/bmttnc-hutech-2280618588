# Chương trình nhập vào một tuple và in ra phần tử đầu tiên và cuối cùng

def print_first_and_last_elements(input_tuple):
    """Hàm in ra phần tử đầu tiên và cuối cùng của một tuple"""
    print("Phần tử đầu tiên:", input_tuple[0])
    print("Phần tử cuối cùng:", input_tuple[-1])

# Nhập tuple từ người dùng, cách nhau bởi dấu phẩy
elements = input("Nhập các phần tử của tuple, cách nhau bởi dấu phẩy: ").split(',')

# Tạo tuple từ danh sách
input_tuple = tuple(elements)

# Gọi hàm để in ra phần tử đầu tiên và cuối cùng
print_first_and_last_elements(input_tuple)