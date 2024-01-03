class Course:
    def __init__(self, course_code, course_name, credits, compulsory, teacher, schedule):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.compulsory = compulsory
        self.teacher = teacher
        self.schedule = schedule
    
    def print_course_info(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credits:", self.credits)
        print("Compulsory:", self.compulsory)
        print("Teacher:", self.teacher)
        print("Schedule:", self.schedule)
    
    def modify_course_name(self, new_name):
        self.course_name = new_name
    
    def modify_teacher(self, new_teacher):
        self.teacher = new_teacher
    
    def modify_schedule(self, new_schedule):
        self.schedule = new_schedule
    
    def get_schedule(self):
        return self.schedule
    
    def get_teacher(self):
        return self.teacher

# 建立物件
c1 = Course("CS101", "Introduction to Computer Science", 3, "Compulsory", "Dr. Smith", "Monday 10:00 AM")
c2 = Course("ENG202", "Advanced English Writing", 2, "Elective", "Prof. Johnson", "Wednesday 2:00 PM")

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
