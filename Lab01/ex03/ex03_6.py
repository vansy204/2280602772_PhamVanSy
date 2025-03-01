def xoaPhanTu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
    else:
        return False
    return dictionary

myDict = {'a':1,'b':2,'c':3 ,'d':4}
keyToDel = 'b'
result = xoaPhanTu(myDict,keyToDel)
if result:
    print("Xóa phần tử thành công")
    print("Dictionary sau khi xóa: ", result)
else:  
    print("Không tìm thấy phần tử cần xóa")