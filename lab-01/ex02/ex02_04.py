# Hiển thị các số từ 2000 đến 3200 chia hết cho 7 và không phải là bội số của 5

result = []
for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

print(", ".join(result))