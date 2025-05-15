# Chương trình đếm số lần xuất hiện của các từ trong chuỗi, các từ cách nhau bởi dấu phẩy

# Nhập chuỗi từ người dùng, các từ cách nhau bởi dấu phẩy
input_string = input("Nhập chuỗi các từ, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các từ
words = input_string.split(',')

# Đếm số lần xuất hiện của từng từ
word_count = {}
for word in words:
    word = word.strip()  # Loại bỏ khoảng trắng thừa
    word_count[word] = word_count.get(word, 0) + 1

# Hiển thị kết quả
print("Số lần xuất hiện của các từ:")
for word, count in word_count.items():
    print(f"{word}: {count}")