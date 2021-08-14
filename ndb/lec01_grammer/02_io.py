import sys

# 공백 기준으로 입력
# a, b, c = map(int, input().split())
# print(a, b, c)

# print(list(map(int, '1 2 3'.split())))

# 전형적인 입력 예
# data 개수
# n = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# print(data)


# 고속 입력 받기
# rstrip() 입력된 엔터등 제거
# str = sys.stdin.readline().rstrip()
# print(str)
# print("<--- has 'enter'?")

print('요러면 개행이 안되지롱', end=' ')
print('something')

answer = 7
print('정답은 ', answer, ' 입니다')
print('정답은 ' + str(answer) + ' 입니다')
print(f'파이썬 3.6부터 이런게 f-string이 지원이 되요, 그리고 정답은 {answer} 이죠')
