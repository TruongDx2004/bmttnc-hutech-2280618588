# Chương trình kiểm tra số nguyên tố

# Hàm kiểm tra số nguyên tố
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Nhập số nguyên từ người dùng
num = int(input("Nhập một số nguyên: "))

# Kiểm tra và hiển thị kết quả
if is_prime(num):
    print(f"{num} là số nguyên tố.")
else:
    print(f"{num} không phải là số nguyên tố.")