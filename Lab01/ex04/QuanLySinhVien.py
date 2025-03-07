from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if sv._id > maxId:
                    maxId = sv._id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return len(self.listSinhVien)
    def nhapSinhVien(self):
        svId= self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        average_score = float(input("Nhập điểm trung bình: "))
        sv = SinhVien (svId,name,sex,major,average_score)
        self.xepLoai(sv)
        self.listSinhVien.append(sv)
    def updateSinhVien(self,ID):
        sv:SinhVien = self.findById(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            average_score = float(input("Nhập điểm trung bình: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.average_score = average_score
            self.xepLoai(sv)
        else:
            print("Không tìm thấy sinh viên cần sửa")
    def sortById(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse=False)
    def sortByScore(self):
        self.listSinhVien.sort(key=lambda x: x.average_score, reverse=True)
    def findById(self,ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None
    def findByName(self,name):
        result = []
        for sv in self.listSinhVien:
            if sv._name == name:
                result.append(sv)
        return result
    def deleteById(self,ID):
        sv = self.findById(ID)
        if sv != None:
            self.listSinhVien.remove(sv)
            return True
        return False
    def xepLoai(self,sv):
        if sv.average_score >= 8:
            sv.rank = "Giỏi"
        elif sv.average_score >= 6.5:
            sv.rank = "Khá"
        elif sv.average_score >= 5:
            sv.rank = "Trung bình"
        else:
            sv.rank = "Yếu"
    def showList(self):
        print("{:<8} {:18} {:8} {:8} {:8} {:8}".format("ID","Name","Sex","Major","Score","Rank"))
        if(listSinhVien.__len__() >0):
                
            for sv in self.listSinhVien:
                print("{:<8} {:18} {:8} {:8} {:8} {:8}".format(sv.id,sv.name,sv.sex,sv.major,sv.average_score,sv.rank)) 
    def getList():
        return listSinhVien
                                                           



    