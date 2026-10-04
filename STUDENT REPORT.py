#STUDENT REPORT:

class Report:

    #CLASS VARIABLE- DEFAULT TEMPLET
    template ="student report"
    

    def __init__(self, student_name, student_marks):
        self.name = student_name
        self.marks = student_marks

    def display_report(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

s1 = Report("GAJANAN", 95)
s2 = Report("JAYDEEP", 85)

s1.display_report()
s2.display_report()