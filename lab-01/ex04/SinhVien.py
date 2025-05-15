# Quản lý sinh viên

class SinhVien:
    ma_tu_dong = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.ma = SinhVien.ma_tu_dong
        SinhVien.ma_tu_dong += 1
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_trung_binh = diem_trung_binh

    def hoc_luc(self):
        if self.diem_trung_binh >= 8:
            return "Giỏi"
        elif 6.5 <= self.diem_trung_binh < 8:
            return "Khá"
        elif 5 <= self.diem_trung_binh < 6.5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"Mã: {self.ma}, Tên: {self.ten}, Giới tính: {self.gioi_tinh}, Chuyên ngành: {self.chuyen_nganh}, Điểm TB: {self.diem_trung_binh}, Học lực: {self.hoc_luc()}"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them_sinh_vien(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        sv = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.danh_sach.append(sv)

    def cap_nhat_sinh_vien(self, ma, ten=None, gioi_tinh=None, chuyen_nganh=None, diem_trung_binh=None):
        for sv in self.danh_sach:
            if sv.ma == ma:
                if ten: sv.ten = ten
                if gioi_tinh: sv.gioi_tinh = gioi_tinh
                if chuyen_nganh: sv.chuyen_nganh = chuyen_nganh
                if diem_trung_binh: sv.diem_trung_binh = diem_trung_binh
                print("Cập nhật thành công!")
                return
        print("Không tìm thấy sinh viên!")

    def xoa_sinh_vien(self, ma):
        self.danh_sach = [sv for sv in self.danh_sach if sv.ma != ma]
        print("Xóa thành công!")

    def tim_kiem_theo_ten(self, ten):
        ket_qua = [sv for sv in self.danh_sach if ten.lower() in sv.ten.lower()]
        return ket_qua

    def sap_xep_theo_diem_tb(self):
        self.danh_sach.sort(key=lambda sv: sv.diem_trung_binh, reverse=True)

    def sap_xep_theo_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda sv: sv.chuyen_nganh)

    def hien_thi_danh_sach(self):
        for sv in self.danh_sach:
            print(sv)
