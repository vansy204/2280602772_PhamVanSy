def demSoLanXuatHien(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
inputStr = input("Nhập list: ")
numbers = inputStr.split()
numbers = list(map(int, numbers))
print("Số lần xuất hiện của các phần tử trong list là: ", demSoLanXuatHien(numbers))
