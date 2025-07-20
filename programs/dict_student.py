#printing only the student who got more than 90 marks
def student_marks(n,m):
    diction = {}
    marks = []
    for i in range(n):
        name = input(f"Enter name of student {i + 1}:")
        for k in range(m):
            mark = int(input(f"Enter mark for subject  {k + 1}:"))
            marks.append(mark)
            diction[name] = marks
    return diction


n = int(input("Enter no of records :"))
m = int(input("Enter no of subjects:"))
xx = student_marks(n,m)
print("Students who got more than 90 as avergae : ")
for k,v in xx.items():
    avg = sum(v) / len(v)
    if avg > 90 :
        print(k)



