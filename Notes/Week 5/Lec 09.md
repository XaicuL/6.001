
# **Classes and Inheritance**

**1. 클래스 설계의 핵심 (Class Implementation)**

클래스를 이용해 새로운 객체 타입(Abstract Data Types)을 정의할 때는 두 가지를 명확히 구분해야 한다

• **What is the object:** 데이터 속성 (Data attributes) - 이 객체가 무엇을 가지는지 정의.

• **How to use the object:** 메서드 (Methods) - 이 객체를 어떻게 사용할 수 있는지 정의.

**2. 정보 은닉과 Getter/Setter (Information Hiding)**

객체 내부의 데이터를 외부에서 함부로 조작하지 못하게 보호하는 객체 지향의 중요 원칙

• **개념:** 외부 프로그래머가 객체의 내부 구현 방식(Implementation)을 모르더라도 추상화된 기능(Abstraction)만으로 사용할 수 있게 만드는 것

• **Getter:** 내부 데이터를 안전하게 읽어오는(반환하는) 메서드.

• **Setter:** 내부 데이터를 안전한 규칙에 따라서만 수정하게 해주는 메서드.

**3. 클래스 변수 (Class Variables)**

• 인스턴스마다 각각 다르게 가지는 변수(`self.variable`)와 다르다.

• 해당 클래스로 만들어진 **모든 인스턴스가 공통으로 하나를 공유**하는 변수

**4. ★ 핵심: 상속 (Inheritance)**

기존에 만든 클래스의 기능을 그대로 물려받아 새로운 클래스를 만드는 강력한 기능

• **Superclass (부모/상위 클래스):** 공통적인 속성과 메서드를 정의해 둔 기본 클래스

• **Subclass (자식/하위 클래스):** 부모의 기능을 물려받으면서, 자신만의 고유한 기능을 추가하거나 부모의 기능을 덮어쓰기(Override)할 수 있는 클래스 

    ◦ _예:_ _Person_ _클래스를 상속받아_ _MIT_person_ _클래스나_ _Student_ _클래스를 만듦._