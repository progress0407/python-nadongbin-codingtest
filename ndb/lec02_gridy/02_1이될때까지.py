print('___ 내 풀이 ___')
# N, K = map(int, input().split())
N, K = 17, 4
count = 0
while N > 1:
    while N % K != 0:
        N -= 1
        count += 1
    N //= K
    count += 1
print(count)

print('___ 동빈님의 풀이 ___')
# 반복문 순회를 할 때마다 나누는 것을 보장하기 때문에
# 밑이 K인 log 시간 복잡도로 줄일 수 있음

n, k = map(int, input().split())
result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n -= result
    if n < k:
        break
    n //= k
    result += 1
result += (n - 1)
print(result)
