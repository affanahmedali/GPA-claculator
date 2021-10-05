class student:
    def input (self):
        self.name = input('Enter name: ')
        self.roll_no = input('Enter roll no: ')
        self.email = input('Enter email Id: ')

    def course_lst(self):
        self.c_lst= list()
        self.courses = int(input("Enter no of course: "))
        for i in range (self.courses):
            self.c_lst.append (input(f"Enter name of course {i+1}: "))
    
    def input_marks(self):
        self.marks_lst = list()
        for i in range(len(self.c_lst)):
            self.marks_lst.append(int(input(f'Enter marks of {self.c_lst[i]}: ')))
    
    def calc_GP(self):
        self.GP_lst = list()
        for i in range (len(self.marks_lst)):
            self.marks = self.marks_lst[i]
            if 100>= self.marks >=85:
                self.GP_lst.append(4.0)
            elif 84>= self.marks >= 80:
                self.GP_lst.append(3.7)
            elif 79>= self.marks >=75:
                self.GP_lst.append(3.4)
            elif 74>= self.marks >=70:
                self.GP_lst.append(3.0)
            elif 69>= self.marks >=67:
                self.GP_lst.append(2.7)
            elif 66>= self.marks >=64:
                self.GP_lst.append(2.4)
            elif 63>= self.marks >= 60:
                self.GP_lst.append(2.0)
            elif 59> self.marks >= 57:
                self.GP_lst.append(1.7)
            elif 56>= self.marks >=54:
                self.GP_lst.append(1.4)
            elif 53>= self.marks >= 50:
                self.GP_lst.append(1.0)
            elif self.marks <=49:
                self.GP_lst.append(0.0)

    def input_credit_hr(self):
        self.credit_hr_lst = list()
        for i in range (len(self.GP_lst)):
            self.credit_hr_lst.append(int(input(f'Enter credit hours of {self.c_lst[i]}: ')))
    
        self.total_credit_hr= sum(self.credit_hr_lst)

    def calc_GPA(self):
        self.GPA_lst = list()
        for i in range(len(self.credit_hr_lst)):
            self.GPA_lst.append((self.credit_hr_lst[i]*self.GP_lst[i]))

        self.GPA = sum(self.GPA_lst)/self.total_credit_hr

    def print(self):
        print(f'Name: {self.name}\nRoll no: {self.roll_no}\nE-mail Address: {self.email}')

        for i in range (len(self.c_lst)):
            print(f'Grade Point {self.c_lst[i]}: {self.GP_lst[i]}')

        print(f'GPA: {self.GPA}')
            

s=student()
s.input()
s.course_lst()
s.input_marks()
s.calc_GP()
s.input_credit_hr()
s.calc_GPA()
s.print()
