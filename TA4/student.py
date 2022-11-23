from Person import Person
from human_being import human_being
class student(Person):
    def __init__(self,age,name,id):
        super().__init__(age,name,id)
        self.grades={}

    def __str__(self):
        return f"name:{self.name}, id:{self.id}, grades: {self.grades}"

    def __repr__(self):
        # return self.__str__()
        return f"name:{self.name}, id:{self.id}, grades: {self.grades}"

    def add_grade(self,c_name, grade):
        self.grades[c_name]=grade

    def avg(self):
        avg=0
        for grade1 in self.grades.values():
            avg+=grade1
        avg=avg/len(self.grades)
        return avg

    def __eq__(self, other_student): # ==
        return self.id==other_student.id

    def __gt__(self, other): # >
        return self.avg()>other.avg()

    def __lt__(self, other): # <
        return self.avg()<other.avg()

    def __add__(self, other): # +
        return (self.avg()+other.avg())/2

    def print_hello(self,msg):
        # print("im student num", self.id)
        super().print_hello(msg)
        print("and im a student")


s1= student(19,"yossi","123456789")
s2 = student(21,"dani", "123456788")
if s1==s2:
    print("yhaaa")
else:
    print("NOO")
s1.add_grade("algebra", 88)
s1.add_grade("py", 98)
s1.add_grade("Math", 60)
s2.add_grade("algebra", 67)
s2.add_grade("py", 78)
s2.add_grade("Math", 98)
s3=s1+s2
s3 = student(12,"yoni", "123456787")
print(s1==s2)
if s1>s2:
    print("S1")
else:
    print("S2")
print(s1.avg())
print(s2.avg())
print(s1+s2)
print(s1)
s1.get_gender()
s1.print_hello("dfsdfgsdgsr")
st_list=[s1,s2,s3]
print(st_list)
s1.add_grade("python",100)
print(s1)
print(s1.grades)
s1.print_hello("adasd")

