def chiaHetCho5(soNhiPhan):
    soThapPhan = int(soNhiPhan, 2)
    if soThapPhan % 5 == 0:
        return True
    else:
        return False
chuoiSoNhiPhan = input("Nhập số nhị phân: ")

soNhiPhanList = chuoiSoNhiPhan.split(",")
soChiaHetCho5 = [so for so in soNhiPhanList if chiaHetCho5(so)]
if(len(soChiaHetCho5) > 0):
    print("Các số chia hết cho 5 là: ", ",".join(soChiaHetCho5))
else:
    print("Không có số nào chia hết cho 5")