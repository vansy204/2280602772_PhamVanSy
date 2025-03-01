def daoNguocList(lst):
    return lst[::-1]
inputList = input("Nhập list: ")
numbers = inputList.split(",")
numbers = list(map(int, numbers))
listDaoNguoc = daoNguocList(numbers)
print("List đảo ngược là: ", listDaoNguoc)