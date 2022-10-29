student=["Rabbi",918822,"Computer","Hafiz",918765,"Computer","Rokon",133397,"Computer","Hassan",682655,"Envt","Masud Rana",658892,"Envt"]
student[9]="Adnan Hassan"
student[11]="Environmental"
student[14]="Environmental"
print(student)


teacher=["Rohim",2012,"Computer","Korim",2012,"Environmental","Jecap",2015,"Electronics"]
teacher.append("Elips")
teacher.append(2015)
teacher.append("Electrical")
print(teacher)



t=["Computer",1822,"Charles Babbage","Electronics",1897,"J.A. Fleming","Electrical",1700,"Benjamin Franklin","Environmental",1960,"Human"]
t[11]="Mora banaici"
t.append("Make")
t.insert(11,"Make")
t.extend(["Human","Make it","Polluted"])
t.index("Polluted")
print(t)






def x (*args):
    sum = 0
    for result in args:
        sum += result
    return sum
rab = x(35,175,52)
print("rab your Total Amoount :",rab)




















