
### 2- 예1 : Syntax Error ###
# print(3 +)

### 2 - 예2 : Static Semantics Error ###
# print('Helloworld' / 5)

### 2 - 예3 : Semantics Error ###
#object : 10과 20의 평균인 15를 구하기 위함

# a = 10
# b = 20
#
# avg1 = a+b / 2
# avg2 = (a+b) / 2
#
#
# print('avg1 = ',avg1) #20.0 (False)
# print('avg2 = ',avg2) #15.0 (True)

### 3 - 예1 : Implicit ###

# print(3+1.5)

### 3 - 예2 : Explicit ###

# x = "10"
# y = 5
#
# print(int(x) + y)

### 3 - 예2 - 1 : ~ Explicit ###

# x = "10"
# y = 5
#
# print(x+ y)

### 명시적 형 변환 Example ###

# x1 = 3
# x2 = 3.0
# x3 = False
#
# x1a = float(x1)
# x2a = int(x2)
#
# print('x1 type : ',type(x1))
# print('x2 type : ',type(x2))
# print('x3 type : ',type(x3))
#
# print('---------------Type Conversion-----------------')
#
# print('x1a : int to float')
# print('x1a type : ',type(x1a))
#
# print('x2a : float to int')
# print('x2a type : ',type(x2a))

### 4 - 예1 : Remark 2 ###

# radius = 2.2
# print('1st radius',radius)
#
# area = 3.14 * (radius ** 2)  # (1) 시점: area는 15.19...
#
# radius = radius + 1    # (2) 시점: radius가 3.2로 재할당됨
# print('2nd radius',radius)

