from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1):
    print("1. Nhập thông tin sinh viên")
    print("2. Sửa thông tin sinh viên")
    print("3. Xóa sinh viên")
   
    print("4. Tìm sinh viên theo ID")
    print("5. Tìm sinh viên theo tên")
    print("6. Hiển thị danh sách sinh viên")
    print("7. Sắp xếp sinh viên theo chuyen nganh")
    print("0. Thoát")
    
    key = int(input("Nhập lựa chọn: "))
    if(key ==1):
        qlsv.nhapSinhVien()
    elif(key ==2):
        if(qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhập ID sinh viên cần sửa: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==3):
        if(qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhập ID sinh viên cần xóa: "))
            if(qlsv.deleteById(ID)):
                print("Xóa thành công")
            else:
                print("Xóa thất bại")
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==4):
        if(qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhập ID sinh viên cần tìm: "))
            sv = qlsv.findById(ID)
            if(sv != None):
                print(sv)
            else:
                print("Không tìm thấy sinh viên")
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==5):
        if(qlsv.soLuongSinhVien() > 0):
            name = input("Nhập tên sinh viên cần tìm: ")
            result = qlsv.findByName(name)
            if(len(result) > 0):
                for sv in result:
                    print(sv)
            else:
                print("Không tìm thấy sinh viên")
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==6):
        if(qlsv.soLuongSinhVien() > 0):
            qlsv.show()
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==7):
        if(qlsv.soLuongSinhVien() > 0):
            qlsv.sortByMajor()
        else:
            print("Danh sách sinh viên rỗng")
    elif(key ==0):
        break
    else:
        print("Lựa chọn không hợp lệ")