# 2 3 1 2 2
li = [2, 3, 1, 2, 2]

li = sorted(li, reverse=True)

group_cnt = 0
for i in li:
    if i <= len(li):
        group_cnt += 1
        li.pop(0)
        for _ in range(i - 1):
            li.pop(li.index(min(li)))

print(group_cnt)