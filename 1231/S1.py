class Student:
    def __init__(self, id, name, major):
        self.__id = id
        self.__name = name
        self.__major = major

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_major(self):
        return self.__major

# 創建學生物件
s1 = Student('STUST001', 'AA', '資工')
print("學生s1姓名=", s1.get_name())
print("學生s1id=", s1.get_id())
print("學生s1科系=", s1.get_major())

s2 = Student('STUST002', 'BB', '資工')
print("學生s2姓名=", s2.get_name())
print("學生s2id=", s2.get_id())
print("學生s2科系=", s2.get_major())
