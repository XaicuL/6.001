
# **Program Efficiency & Big-O**

**1. 프로그램 효율성 평가 방법 (Evaluating Efficiency)**

코드가 얼마나 빠른지 측정하는 세 가지 접근법이 있다

• **시간 측정 (Timing):** `time` 모듈 사용. 컴퓨터 성능이나 구현 방식에 따라 결과가 달라져서 일관성이 없음

• **연산 횟수 세기 (Counting Operations):** 수학 연산, 비교 등을 세는 방식. 입력 크기에 따른 관계를 볼 수 있지만 여전히 구현 방식에 의존적임

• **★ 성장률의 차수 (Order of Growth):** 알고리즘 자체의 스케일링 능력을 평가하기 위해 입력 크기(Input size)가 무한히 커질 때의 동작을 추상적으로 평가하는 가장 좋은 방법 

**2. 측정의 세 가지 경우 (Cases)**

입력 데이터의 상태에 따라 실행 시간이 달라짐을 알아야 한다.

• **Best Case (최선):** 원하는 값이 리스트의 맨 앞에 있는 경우. (최소 실행 시간) 

• **Average Case (평균):** 실용적인 지표지만 정확히 계산하기 어려움

• **★ Worst Case (최악):** 원하는 값이 리스트에 아예 없는 경우. (최대 실행 시간). **알고리즘 분석의 핵심 기준 (병목 지점 파악)** 

**3. Big-O 표기법 (Big Oh Notation,** O**)**

최악의 경우(Worst case)에 프로그램 실행 시간이 어떻게 증가하는지 
상한선(Upper bound)을 나타내는 표기법

• **핵심 규칙:**

   ◦ 상수 덧셈, 곱셈은 무시합니다 (예: O(3n+2)→O(n)) 

   ◦ 가장 빠르게 증가하는 **지배적인 항(Dominant term)**만 남깁니다 (예: O(n2+n)→O(n2)) 

**4. 복잡도 계산 법칙 (Analyzing Complexity)**

• **덧셈 법칙 (Law of Addition):** 순차적인(Sequential) 구문일 때 사용.

   ◦ O(f(n))+O(g(n))=O(f(n)+g(n)) (둘 중 큰 것만 남음) 

• **곱셈 법칙 (Law of Multiplication):** 중첩 루프(Nested loops)일 때 사용.

   ◦ O(f(n))×O(g(n))=O(f(n)×g(n)) 

**5. 복잡도 클래스 (Complexity Classes)**

성장 속도가 느린 것(좋은 것)부터 빠른 것(나쁜 것) 순서

1. O(1)**:** Constant (상수 시간) - 최고 효율 

2. O(logn)**:** Logarithmic (로그 시간) 

3. O(n)**:** Linear (선형 시간) - 단순 반복문 

4. O(nlogn)**:** Log-linear (로그 선형 시간)

5. O(nc)**:** Polynomial (다항 시간) - 중첩 루프 (n2,n3 등)

6. O(cn)**:** Exponential (지수 시간) - 최악의 효율 (예: 단순 재귀 피보나치, 하노이의 탑) 