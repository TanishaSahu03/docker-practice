class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def display(self):
        return self.name + str(self.age)

    def show_id(self):
        return self.id

if __name__ == "__main__":
    student1 = Student("Ram", 20, 2)
    print(student1.display())
    print(student1.show_id())
