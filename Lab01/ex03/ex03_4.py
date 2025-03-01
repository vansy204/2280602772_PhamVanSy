def truyCapPhanTu(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement

inputTuple = input("Nhập tuple: ")
first,last = truyCapPhanTu(inputTuple)
print("Phần tử đầu tiên và cuối cùng của tuple là: ", first, last)
