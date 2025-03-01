soGioLam = float(input("Nhập số giờ làm: "))
luongGio = float(input("Nhập lương mỗi giờ: "))
gioTieuChuan = 44
gioVuotChuan = max (0,soGioLam,gioTieuChuan)

thucTinh  = gioTieuChuan * luongGio + gioVuotChuan * luongGio * 1.5

print("Lương của bạn là: ", thucTinh)