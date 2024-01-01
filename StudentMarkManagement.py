import os
clear = lambda: os.system('cls')
clear()

Student_List = []
Course_List = []
Mark_List = []

Number_of_Student = input("Enter Number of Student: ")
for i in range(1, int(Number_of_Student) + 1):
    Student_Information_Tab = {
        "Name": "Null",
        "ID" : "Null",
        "DoB" : "Null",
    }
    print("Enter information for student " + str(i))
    
    Student_Information_Tab.update({"Name": input("Name: ")})
    Student_Information_Tab.update({"ID": input("ID: ")})
    Student_Information_Tab.update({"DoB": input("Date of Birth: ")})
    clear()
    Student_List.append(Student_Information_Tab)

Number_of_Course = input("Enter Number of Courses: ")
for i in range(1, int(Number_of_Course) + 1):
    Course_infomation_tab = {
        "Name":"Null",
        "ID":"Null"
    }
    
    print("Enter information for Course " + str(i))
    Course_infomation_tab.update({"Name": input("Name: ")})
    Course_infomation_tab.update({"ID": input("ID: ")})
    clear()
    Course_List.append(Course_infomation_tab)
    
for i in range(0, int(Number_of_Course)):
    Mark__Per_Coures_List = []
    print("Enter Mark For " + Course_List[i].get("Name") + "Course")
    
    for j in range(0, int(Number_of_Student)):
        print(Student_List[j].get("Name"))
        Mark_information_Tab = {
            "Name":"Null",
            "Mark":"Null"
        }
        Mark_information_Tab.update({"Name": Student_List[j].get("Name")})
        Mark_information_Tab.update({"Mark": input(" Mark: ")})
        Mark__Per_Coures_List.append(Mark_information_Tab)
    
    Mark_List.append(Mark__Per_Coures_List)

print("-Student List-")
for i in range(0, int(Number_of_Student)):
    print(Student_List[i].get("Name") +"|" + Student_List[i].get("ID") + "|" + Student_List[i].get("DoB"))

print("----------------------------------------------------------------------------------------------------")

print("-Course List-")
for i in range(0,int(Number_of_Course)):
    print(Course_List[i].get("Name") + "|" + Course_List[i].get("ID"))
print("----------------------------------------------------------------------------------------------------")
 
for i in range(0, int(Number_of_Course)):
    print("Student Mark of " + Course_List[i].get("Name") +" Course")
    for j in range(0, int(Number_of_Student)):
        print(Mark_List[i][j].get("Name") + ":"+ Mark_List[i][j].get("Mark"))
        
