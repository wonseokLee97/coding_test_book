n = int(input())
x, y = 1, 1
plans = input().split()

L = 0, -1
R = 0, +1
U = +1, 0
D = -1, 0

dx = [0, 0, -1, 1]
dy = [-1, +1, 0, 0]

steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + steps[i][0]
            ny = y + steps[i][1]

    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)


