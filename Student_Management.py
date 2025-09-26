class StudentDatabase:
    student_list = []
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

class Student:
    def __init__(self , student_id , name , department):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = False
        StudentDatabase.add_student(self)
        
    def get_id(self):
        return self._student_id
    
    def enroll_student(self):
        
        if not self._is_enrolled:
            self._is_enrolled = True
            print(f"Student {self._student_id} has been enrolled.")
        
        else:
            print(f"Student {self._student_id} is already enrolled.")
        
    def drop_student(self):
        if self._is_enrolled:
            self._is_enrolled = False
            print(f"Student {self._student_id} has been dropped.")
        else:
            print(f"Student {self._student_id} is not yet enrolled.")


    def view_student_info(self):
        status = "Enrolled" if self._is_enrolled else "Not Enrolled"
        print("-----------------------------------")
        print(f"Student ID:     {self._student_id}")
        print(f"Name:           {self._name}")
        print(f"Department:     {self._department}")
        print(f"Status:         {status}")
        print("-----------------------------------")

    def find_student(student_id):
        for student in StudentDatabase.student_list:
            if student.get_id() == student_id:
                return student
        return None
    


def main():
    # Students
    Student("1001", "Sajid", "Computer Science")
    Student("1002", "Arafat", "Mathematics")
    Student("1003", "Nabila", "Physics")
    print("\n--- Student Management System ---")
    while True:
        print("\nMenu:")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Add Exit")

        user_input = input("Enter your choice (1-4): ")


        if user_input == '1':
            print("\n--- All Students ---")
            if not StudentDatabase.student_list:
                print("No students in the database.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif user_input == '2':
            print("\n--- Enroll Student ---")
            student_id = input("Enter Student ID to enroll: ")
            student = Student.find_student(student_id)
            if student:
                student.enroll_student()
            else:
                print(f"No student found with ID {student_id}.")

        elif user_input == '3':
            print("\n--- Drop Student ---")
            student_id = input("Enter Student ID to drop: ")
            student = Student.find_student(student_id)
            if student:
                student.drop_student()
            else:
                print(f"No student found with ID {student_id}.")


        elif user_input == '4':
            print("Good bye!")
            break                

        else:
            print("Invalid. Please enter a number between 1 and 4.")    

if __name__ == "__main__":
    main()