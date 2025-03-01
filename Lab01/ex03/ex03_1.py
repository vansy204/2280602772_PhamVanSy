def tinhTongSoChan(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
inputList = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")
lst = inputList.split(",")
lst = list(map(int, lst))

print("Tổng các số chẵn trong dãy là: ", tinhTongSoChan(lst))
