from QuanLySinhVien import QuanLySinhVien # type: ignore

qlsv = QuanLySinhVien()

def menu():
    
    while True:
        print("\n--- Quản Lý Sinh Viên ---")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa một sinh viên")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp danh sách theo điểm trung bình")
        print("6. Sắp xếp danh sách theo tên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            ten = input("Nhập tên: ")
            gioi_tinh = input("Nhập giới tính: ")
            chuyen_nganh = input("Nhập chuyên ngành: ")
            diem_trung_binh = float(input("Nhập điểm trung bình: "))
            qlsv.them_sinh_vien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        elif lua_chon == "2":
            ma = int(input("Nhập mã sinh viên cần cập nhật: "))
            ten = input("Nhập tên mới (bỏ trống nếu không thay đổi): ")
            gioi_tinh = input("Nhập giới tính mới (bỏ trống nếu không thay đổi): ")
            chuyen_nganh = input("Nhập chuyên ngành mới (bỏ trống nếu không thay đổi): ")
            diem_trung_binh = input("Nhập điểm trung bình mới (bỏ trống nếu không thay đổi): ")
            diem_trung_binh = float(diem_trung_binh) if diem_trung_binh else None
            qlsv.cap_nhat_sinh_vien(ma, ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        elif lua_chon == "3":
            ma = int(input("Nhập mã sinh viên cần xóa: "))
            qlsv.xoa_sinh_vien(ma)
        elif lua_chon == "4":
            ten = input("Nhập tên sinh viên cần tìm: ")
            ket_qua = qlsv.tim_kiem_theo_ten(ten)
            if ket_qua:
                print("Kết quả tìm kiếm:")
                for sv in ket_qua:
                    print(sv)
            else:
                print("Không tìm thấy sinh viên!")
        elif lua_chon == "5":
            qlsv.sap_xep_theo_diem_tb()
            print("Danh sách đã được sắp xếp theo điểm trung bình!")
        elif lua_chon == "6":
            qlsv.sap_xep_theo_chuyen_nganh()
            print("Danh sách đã được sắp xếp theo tên ngành!")
        elif lua_chon == "7":
            print("Danh sách sinh viên:")
            qlsv.hien_thi_danh_sach()
        elif lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

# Chạy chương trình
if __name__ == "__main__":
    menu()