class Course:
    def __init__(self, course_code, course_name, credits, compulsory, teacher, schedule):
        # 初始化課程屬性
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.compulsory = compulsory
        self.teacher = teacher
        self.schedule = schedule
    
    def print_course_info(self):
        # 列印課程資訊
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credits:", self.credits)
        print("Compulsory:", self.compulsory)
        print("Teacher:", self.teacher)
        print("Schedule:", self.schedule)
    
    def modify_course_name(self, new_name):
        # 修改課程名稱
        self.course_name = new_name
    
    def modify_teacher(self, new_teacher):
        # 修改任課老師
        self.teacher = new_teacher
    
    def modify_schedule(self, new_schedule):
        # 修改上課時間
        self.schedule = new_schedule
    
    def get_schedule(self):
        # 取得上課時間
        return self.schedule
    
    def get_teacher(self):
        # 取得任課老師
        return self.teacher
    
    def set_compulsory(self, is_compulsory):
        # 設置必選修狀態
        self.compulsory = is_compulsory
    
    def get_course_code(self):
        # 取得課程代碼
        return self.course_code
    
    def get_course_name(self):
        # 取得課程名稱
        return self.course_name
    
    def get_credits(self):
        # 取得學分數
        return self.credits
    
    def is_compulsory(self):
        # 判斷是否必選修
        return self.compulsory
    
    def get_course_info(self):
        # 取得課程全部資訊
        return {
            "Course Code": self.course_code,
            "Course Name": self.course_name,
            "Credits": self.credits,
            "Compulsory": self.compulsory,
            "Teacher": self.teacher,
            "Schedule": self.schedule
        }

# 建立物件
c1 = Course("CS101", "Introduction to Computer Science", 3, True, "Dr. Smith", "Monday 10:00 AM")

# 印出課程資訊
c1.print_course_info()
print()

# 修改課程名稱
c1.modify_course_name("Intro to CS")

# 修改任課老師
c1.modify_teacher("Dr. Brown")

# 修改上課時間
c1.modify_schedule("Monday 11:30 AM")

# 再次印出課程資訊
c1.print_course_info()

# 使用其他副函式
print("Course Code:", c1.get_course_code())
print("Is Compulsory:", c1.is_compulsory())
print("Course Info:", c1.get_course_info())
