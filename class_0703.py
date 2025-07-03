
class Person():
    # 初始化預設設定    
    #                  參數1 參數2
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi! My name is {self.name}. I'm {self.age} years old."
    
    def is_adult(self):
        return self.age >= 18

    def set_age(self, new_age):
        if new_age <= 0:
            print('年齡不能為負數')
        else:
            self.age = new_age


# 實例化(呼叫物件)
person_1 = Person("Alice", 20)
# print(person_1.name)
# print(person_1.age)
# print(person_1.introduce())
# print(person_1.is_adult())
# person_1.set_age(22)
# print(person_1.age)  # 修改後年齡


# 創立第二個人
# person_2 = Person("Bob", 15)
# print(person_2.name)
# print(person_2.age)
# print(person_2.introduce())
# print(person_2.is_adult())


# Student 物件繼承 Person 物件功能以及 super().__init__
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        """
        這裡使用 super().__init__(name, age) 引用 Person 的 
        self.name = name
        self.age = age
        """
        self.student_id = student_id
        self.grade = grade
        self.scores = {}


    def study(self):
        return f"I'm {self.name}. I'm studying in grade {self.grade}. My ID is {self.student_id}"


    def scores_data(self, subject, score):
        self.scores[subject] = score
        return self.scores
        



student_1 = Student('Amy', 9, 'S30323', 3)
# print(student_1.age)  # 從 Person()繼承來的
# print(student_1.name)  # 從 Person()繼承來的
# print(student_1.student_id)
# print(student_1.grade)
# print(student_1.introduce()) # 從 Person()繼承來的
# print(student_1.is_adult()) # 從 Person()繼承來的
# print(student_1.study())
# print(student_1.scores_data('math', 90))
# print(student_1.scores_data('eng', 95))
# print(student_1.scores_data('math', 85))

"""
題目:
做一個物件叫做 Pet
參數有 name, animal_type, age
設計一個功能叫做 pet_info
會回傳 {"name":XXX ,"animal_type":XXX, age: X}
"""
class Pet():
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.pet_data = {}

    def pet_info(self):
        self.pet_data["name"] = self.name
        self.pet_data["animal_type"] = self.animal_type
        self.pet_data["age"] = self.age
        return self.pet_data
        

