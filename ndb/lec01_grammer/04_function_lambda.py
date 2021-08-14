def add(a, b):
    print('add func')
    return a + b


def sub(a, b):
    return a - b


result = add(3, 7)
print(result)

result = sub(b=7, a=3)
print(result)

a = 100


def global_func():
    global a  # 밖의 a를 사용할 것
    a += 10


for _ in range(10):
    global_func()

print(a)


def global_func():
    print(a)  # 값을 조작이 아닌 참조하는 건 가능


global_func()

li = [1, 2]


def global_func():
    li.append(3)  # 이런 레퍼런스 타입은.. 참조형이기에 가능한것으로 보임. 값을 바꾸지 않는다


global_func()

print(li)

# 함수 안에서는 지역안에서 선언된 데이터를 우선순위로 접근
# 함수 밖에서는 밖에서 선언된 것에 접근 (내부의 지역범위는 소멸됨)


li = [1, 2]


def global_func():
    # global list # 외부에 있는 것을 우선하고자 할때는 global을 사용하면 된다
    li = [5, 4]
    li.append(3)  # 이런 레퍼런스 타입은.. 참조형이기에 가능한것으로 보임. 값을 바꾸지 않는다
    print(li)
    li2 = [1]


global_func()

print(li)


# print(list2) # name list2 is not defined

# 패킹: 여러 개의 반환값을 가질 수 있음

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var


# 언패킹: 값을 풀어서 다시 담음
a, b, c, d = operator(7, 3)
print(a, b, c, d)

print((lambda a, b: a + b)(3, 7))

# 튜플 in 리스트
arr = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(type(arr))
print(arr[0])

for e in arr[0]:
    print(e)

for e1 in arr:
    for e2 in e1:
        print(e2, end=',')
    print()


def my_key(x):
    return x[1]


print(my_key(arr))
print(my_key(my_key(arr)))

print(sorted(arr))
# 점수 기준으로 오름차순 정리
print(sorted(arr, key=my_key))
print(sorted(arr, key=lambda x: x[1]))

li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 10]

# 각각의 list를 합한 것을 반환
result = map(lambda a, b: a + b, li1, li2)
print(list(result))

result = sum([1, 2, 3, 4, 5])
print(result)

# min, max
# min_result = min(3, 5, 7, 2)
# max_result = max(3, 5, 7, 2)
li = [3, 5, 7, 2]
min_result, max_result = min(li), max(li)
print(min_result, max_result)

result = eval('2*5 + 4')
print(result)

li = [9, 1, 8, 5, 4]
result = sorted(li)
reverse_result = sorted(li, reverse=True)
print(result)
print(reverse_result)

li_tuple = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(li_tuple, key=lambda x: x[1], reverse=True)
print(result)

# 순열 P 과 조합 C
print('___ 순열 ___')
from itertools import permutations, compress

data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)
for e in result:
    print(e)

from itertools import combinations

print('___ 조합 ___')
result = list(combinations(data, 2))
print(result)
for e in result:
    print(e)

print('___ 중복 순열 ___')
from itertools import product

result = list(product(data, repeat=2))
for e in result:
    print(e)

print('___ 중복 조합 ___')
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
for e in result:
    print(e)

print('___ Counter ___')
from collections import Counter

li = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(li)

print(counter['blue'])
print(counter['green'])
print(dict(counter))

print('___  최대 공약수 & 최소 공배수 ___')
import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


a = 14
b = 21
print(math.gcd(a, b))
print(lcm(14, 21))

