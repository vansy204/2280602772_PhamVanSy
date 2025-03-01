def taoTupleTuList(lst):
    return tuple(lst)

inputList = input("Nhập list: ")
numbers = inputList.split(",")
numbers = list(map(int, numbers))
tupleFromList = taoTupleTuList(numbers)
print("List là: ", numbers)
print("Tuple từ list là: ", tupleFromList)
