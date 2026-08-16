import json
from abc import ABC , abstractmethod 
from pathlib import Path

database = "school_data.json"
data={"students" :[] , "Teachers" : []}

if Path(database).exists():
    with open(database , 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(database , 'w') as f:
        json.dump(data,f,indent=4)

#abstract class for reg
class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass  

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


    

class Students(Persons):

    def get_roles(self):
       return "student" 

    def register(self):
        name = input("tell your name:- ")
        age=int(input("Tell your age:- "))
        email = input("Tell your email:- ")
        roll_no=input("tell your roll number:- ")


        if not Persons.validate_email(email):
            print("invalid email")
            return

        for i in data['students']:
            if i['roll_no'] == roll_no:
                print("Student with this Roll_no already exists")
                return

        data['students'].append({
            "name":name,
            "age" : age ,
            "email" : email,
            "roll_no" : roll_no,
            "grades" : {}
        })  
        save()  
        print(f"Student {name} registered") 


    def show_details(self):
        roll_no = (input("Enter your roll no:- "))
        for s in data['students']:
            if s['roll_no'] == roll_no:
                grades=s['grades']
                avg = sum(grades.values()) / len(grades) if grades else 0
                print(f"\nName : {s['name']}")
                print(f"roll no : {s['roll_no']}")
                print(f"grades : {grades}")
                print(f"Average : {avg:.1f}")
                return






    def add_grades(self):
        roll_no=input("Tell your rool no:- ")
        subject=input("enter your subject:- ")
        marks=float(input("Enter your marks:- "))


        for i in data['students']:
            if i['roll_no'] == roll_no:
                i['grades'][subject] = marks

                save()
                print("Grade added succesfully")
                return
        print("student not found")    



class Teacher(Persons):
    def get_roles(self):
        return "Teachers"


    def register(self):
            name = input("tell your name:- ")
            age=int(input("Tell your age:- "))
            email = input("Tell your email:- ")
            subject= input("tell your subject:- ")
            emp_id=input("tell your emp id:- ")


            if not Persons.validate_email(email):
                print("invalid email")
                return


            for i in data['Teachers']:
                if i['emp_id'] == emp_id:
                    print("Teacher with this emp_id already exists")
                    return


            data['Teachers'].append({
                "name":name,
                "age" : age ,
                "email" : email,
                "subject": subject,
                "emp_id" : emp_id
                    })
            save()
            print(f"Teacher {name} registered")

    def show_details(self):
            emp_id = (input("Enter your emp_id:- "))
            for t in data['Teachers']:
                if t['emp_id'] == emp_id:
                
                    print(f"\nName : {t['name']}")
                    print(f"Emp_id : {t['emp_id']}")
                    print(f"Subject: {t['subject']}")
                    return  

            print("Techer not found")    

    
       

stud = Students()

teach = Teacher()

print("Press 1 to register a stuedent")
print("Press 2 to register a Teacher")
print("Press 3 to add grades")
print("Press 4 to  show a detail")
print("Press 5 to show a teacher details")

choice=int(input("please teell your choice : - "))
if choice == 1:
    stud.register()
elif choice==2:
    teach.register()

elif choice==3:
    stud.add_grades()    

elif choice==4:
    stud.show_details() 

elif choice==5:
    teach.show_details()
         
