
# **Object Oriented Programming (OOP)**

**1. 객체 지향 프로그래밍 기초 (OOP Basics)**

파이썬의 모든 데이터(int, float, string, list 등)는 **객체(Object)** 라고 한다.

• **객체의 3요소:**

   ◦ **타입 (Type):** 객체의 종류.

   ◦ **데이터 속성 (Data Representation):** 객체가 무엇(What)인지 나타내는 내부 데이터.

   ◦ **절차적 속성 (Procedures/Methods):** 객체를 어떻게(How) 다룰 수 있는지 정의한 함수 

• **인스턴스 (Instance):** 특정 타입으로 만들어진 실제 객체.
(Ex. `1234`는 `int` 타입의 인스턴스, `"Hello"`는 `string` 타입의 인스턴스) 

**2. 클래스 (Classes)로 나만의 타입 만들기**

파이썬에 내장된 타입 외에, 사용자가 직접 새로운 데이터 타입을 정의할 때 `class` 키워드를 사용한다.

• **구조:**
  - 괄호 안의 `object`는 파이썬의 가장 기본 객체를 **상속(Inherit)** 받는다는 의미

**3. 메서드와** **self** **(Methods & Self)**

클래스 안에 정의되어 그 클래스의 인스턴스만 사용할 수 있는 특별한 함수

• **특징:** 파이썬은 항상 메서드의 **첫 번째 인자로 객체 자신**을 넘겨준다.
이 첫 번째 인자의 이름을 관습적으로 **`self`** 라고 부른다

• **__init__** **메서드:** 객체가 처음 생성될 때 데이터를 초기화하는 특별한 메서드

• **점 표기법 (Dot Notation):** 객체의 데이터 속성이나 메서드에 접근할 때 `.`을 사용한다 (`obj.method()`) 

```

class Student:
    def __init__(self, name, age, gender):
        # 속성 이름 설정
        self.name = name
        self.age = age
        self.gender = gender

    # 메서드 이름을 속성과 다르게 설정 (예: get_name 등)
    def introduce(self):
        return f"{self.name} is a student"

    def get_age(self):
        return f"age : {self.age}"

    def get_gender(self):
        return f"gen : {self.gender}"

# "man"은 문자열로 전달
stu1 = Student("JUN", 21, "man")

print(stu1.introduce())
print(stu1.get_age())

```