from class_0703 import Person  # 從 class_0703.py 引入 Person 物件
from class_0703 import Student
from class_0703 import Pet


def main():
    person = Person("Alice", 20)
    student = Student('Amy', 9, 'S30323', 3)
    pet = Pet("Lucky", "dog", 5)

    print(f"Hi! I'm {person.name}. I have a student, {student.name}. she has a pet, named {pet.name}")
    print(student.introduce())



if __name__ == '__main__':
    main()
