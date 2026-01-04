def tinh_trung_binh(danh_sach_diem):
    tong = sum(danh_sach_diem)
    so_mon = len(danh_sach_diem)
    return tong / so_mon

def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def nhap_diem(ten_mon):
    raw = input(f"Nhập điểm môn {ten_mon} (0-10): ").strip().replace(",", ".")
    try:
        diem = float(raw)
        if diem < 0 or diem > 10:
            return None
        return diem
    except ValueError:
        return None

def nhap_so_mon():
    raw = input("Nhập số môn học: ").strip()
    if raw.isdigit():
        so_mon = int(raw)
        if so_mon > 0:
            return so_mon
    return None

def hien_thi_menu():
    print("\n" + "=" * 45)
    print("PHẦN MỀM XẾP LOẠI HỌC SINH")
    print("=" * 45)
    print("1) Thêm học sinh")
    print("2) Xem danh sách + điểm TB + xếp loại")
    print("0) Thoát")
    print("=" * 45)

danh_sach_hoc_sinh = []

while True:
    hien_thi_menu()
    lua_chon = input("Chọn chức năng: ").strip()

    if lua_chon == "":
        print("Bạn chưa nhập lựa chọn. Vui lòng thử lại.")
        continue

    if lua_chon == "1":
        ten = input("Nhập tên học sinh: ").strip()
        if ten == "":
            print("Tên không được để trống!")
            continue

        so_mon = nhap_so_mon()
        if so_mon is None:
            print("Số môn không hợp lệ! (Phải là số nguyên > 0)")
            continue

        danh_sach_mon = []
        danh_sach_diem = []

        for i in range(so_mon):
            ten_mon = input(f"Nhập tên môn thứ {i+1}: ").strip()
            if ten_mon == "":
                print("Tên môn không được để trống!")
                danh_sach_mon = []
                danh_sach_diem = []
                break

            diem = nhap_diem(ten_mon)
            if diem is None:
                print(f"Điểm môn {ten_mon} không hợp lệ!")
                danh_sach_mon = []
                danh_sach_diem = []
                break

            danh_sach_mon.append(ten_mon)
            danh_sach_diem.append(diem)


        if len(danh_sach_mon) == so_mon:
            hoc_sinh = [ten, danh_sach_mon, danh_sach_diem]
            danh_sach_hoc_sinh.append(hoc_sinh)
            print(f"Đã thêm học sinh: {ten}")


    elif lua_chon == "2":
        if len(danh_sach_hoc_sinh) == 0:
            print("Chưa có học sinh nào trong danh sách.")
            continue

        print("\n--- DANH SÁCH HỌC SINH ---")
        for i in range(len(danh_sach_hoc_sinh)):
            ten = danh_sach_hoc_sinh[i][0]
            ds_mon = danh_sach_hoc_sinh[i][1]
            ds_diem = danh_sach_hoc_sinh[i][2]

            diem_tb = tinh_trung_binh(ds_diem)
            loai = xep_loai(diem_tb)

            print(f"{i+1}. {ten}")

            for j in range(len(ds_mon)):
                print(f"   - {ds_mon[j]}: {ds_diem[j]}")
            print(f"   TB = {diem_tb:.2f}  =>  Xếp loại: {loai}")

    elif lua_chon == "0":
        print("Tạm biệt! Kết thúc chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Hãy nhập 1, 2 hoặc 0.")
