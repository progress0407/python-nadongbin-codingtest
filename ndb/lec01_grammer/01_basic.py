import time

start_time = time.time()

a = -.7
print(a)
print(3e2)
print(int(3e2))

a = 0.3 + 0.6
print(round(a, 4))

if a == 0.9:
    print(True)
else:
    print(False)

print(round(123.456, 2))

print(3 / 2)

n = 10
list = [0] * n
print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[-1])
print(list[-3])
print(list[2:6])  # 끝 index + 1

array = [i for i in range(10)]
print(array)

array = [i + 1 for i in range(10)]
print(array)

array = [2 * i + 1 for i in range(10)]
print(array)

array = [i for i in range(10) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

array = []
for i in range(10):
    if i % 2 == 1:
        array.append(i)

print(array)
# 오류 : array = [i for i+1 in range(10)]

# 반복되는 변수 무시
for _ in range(5):
    print('Hello World')

array = [[0] * 2 for _ in range(4)]
print(array)

array = [[0] * 2] * 4  # 잘못된 예시
# inner list가 모두 같은 곳을 참조함
# 만일 한곳 수정하면 전부다 변경됨

print(array)

n = 4
m = 3
array = [[0] * m for _ in range(n)]
array[1][1] = 1
print(array)

array = [[0] * m] * n
array[1][1] = 1
print(array)

end_time = time.time()

print('_____ [elapsed time} ______: ', end_time - start_time)

list = [3, 1, 4, 2]
list.insert(2, 5)  # 2 번쨰 자리에 5 추가
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(list.count(5))  # 값이 5인 개수
list.append(3)
print(list)
list.remove(3)  # 값이 3인 수를 하나만 제거
print(list)

# 리스트내 특정 값을 가지는 모든 값 제거
list = [1, 2, 3, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in list if i not in remove_set]
print(result)

data = "Hello 'Python'"
print(data)

data = 'Hello "Python"'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = 'Hello'
b = 'World'
print(a + ' ' + b)
print((a + ' ') * 3)
print(a[0:4])
print(a[0])
# a[0]='M'  immutable

tuple = (1, 2, 3, 4, 4, 4)
print(tuple)
print(tuple[0:3])
# tuple[0]=9 immutable

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다 : ", data['사과'])

key_list = data.keys();
value_list = data.values();

print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

for value in value_list:
    print(value)

data = set([1, 1, 2, 2, 3])
print(data)
data = {1, 1, 2, 2, 3}
print(data)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print('합집합: ', setA | setB)
print('교집합: ', setA & setB)
print('차집합: ', setA - setB)

data = {1, 2}
data.add(3)
print(data)
data.update([4, 5])
print(data)
data.remove(3)
print(data)
