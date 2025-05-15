# Tính toán số tiền thực nhận của nhân viên dựa trên giờ làm việc và mức lương theo giờ

# Nhập số giờ làm việc hàng tuần và mức lương theo giờ
hours_worked = float(input("Nhập số giờ làm việc hàng tuần: "))
hourly_rate = float(input("Nhập mức lương theo giờ: "))

# Số giờ tiêu chuẩn mỗi tuần
standard_hours = 44

# Tính toán lương
if hours_worked <= standard_hours:
    total_salary = hours_worked * hourly_rate
else:
    overtime_hours = hours_worked - standard_hours
    total_salary = (standard_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5)

# Hiển thị kết quả
print(f"Số tiền thực nhận của nhân viên là: {total_salary:.2f} VND")