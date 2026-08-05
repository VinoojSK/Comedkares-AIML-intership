subjects=("python","sql","ai")
students=[]
def add_student(name,age):
    student={
        "name":name,
        "age": age,
        "subjects":subjects
    }
    students.append(student)
add_student("vinooj",21)
add_student("vijay raj",20)
add_student("dhanraj",19)
for student in students:
    print(student)
