# 02984
S = '02984'
# S = '11'
result = 0
for s in S:
    i = int(s)
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
