# 가이드라인에서는  4개의 공백 문자가 들여쓰기의 표준이라 정의
# 4번 space VS tab : 2진영

# 범위가 작은 구간부터 해야 모든 상황을 나누어 처리 가능
score = 95
if score >= 95:
    print('학점 A+')
elif score >= 90:
    print('학점 A')
else:
    print('학점 B~F')

# and or not
if (True or False) and (not False):
    print("True")

# in, not in
# 리스트, 튜플, 문자열, 딕셔너리

if 'a' not in 'qwe':
    print(True)

if 1 in [1, 2]:
    print(True)

# pass : 아무고또 하기 시로
if True:
    pass  # 나중에 작성할꼬야

국가기술자격시험_채점결과 = 65
# if 국가기술자격시험_채점결과 >= 60: result="합격"
# else: result="응다시봐"
result = '합격' if 국가기술자격시험_채점결과 > 60 else '응다시봐'
print(result)

x = 4
# 대박.. 수학의 부등식 지원
if (0 < x < 10):
    # if 0 < x and x < 10:
    print(f'x는 0과 10사이의 수입니다 : {x}')

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

arr = [5, 3, 4, 1, 2]
for e in arr:
    print(e)

result = 0
# 인자가 하나시 시작값은 0이 됨
for i in range(1, 10 + 1):
    result += i

print(result)

result = ""
for i in range(10 + 1):
    result += ", " + str(i)

print(result)

# continue, break

score = [93, 67, 86, 92, 78]
cheating_student_list = [1, 3]

for i in range(len(score)):
    if i+1 in cheating_student_list:
        continue # 부정행위 적발
    if score[i] > 70:
        print(f'{i+1}번째 학생 합격입니다! 점수 : {score[i]}')

score = dict()
score['철수'] = 93
score['영희'] = 84
score['민이'] = 64
score['만득이'] = 98
cheating_student_list = {'철수', '만득이'}

for i in score:
    if i in cheating_student_list:
        continue
    if score[i] > 80:
        print(f'{i} 학생 합격입니다 ! 점수: {score[i]}')

for i in range(2,10):
    print(f'_______ {i}단 _______')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
    print()
