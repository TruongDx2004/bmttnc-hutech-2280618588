# Chương trình xóa một phần tử trong một dictionary

def remove_key_from_dict(dictionary, key):
    """Hàm xóa một phần tử trong dictionary theo key"""
    if key in dictionary:
        del dictionary[key]
        print(f"Đã xóa phần tử có key: {key}")
    else:
        print(f"Key '{key}' không tồn tại trong dictionary.")
    return dictionary

# Ví dụ sử dụng
my_dict = {"a": 1, "b": 2, "c": 3}
print("Dictionary ban đầu:", my_dict)

# Nhập key cần xóa
key_to_remove = input("Nhập key cần xóa: ")

# Gọi hàm để xóa phần tử
updated_dict = remove_key_from_dict(my_dict, key_to_remove)

# Hiển thị dictionary sau khi xóa
print("Dictionary sau khi xóa:", updated_dict)