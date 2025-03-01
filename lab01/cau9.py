def kiemTraSoNguyenTo(n):
    if n <=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
number = int (input("Nhập số nguyên: "))
if kiemTraSoNguyenTo(number):
    print(number, "là số nguyên tố")
else:
    print(number, "không phải là số nguyên tố")
    