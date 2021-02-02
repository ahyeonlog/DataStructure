board = [
    [0, 1, 2, 3, 4, 5],
    [2, 2, 3, 4, 5, 6],
    [4, 3, 4, 5, 6, 7],
    [6, 4, 5, 6, 7, 8],
    [8, 5, 6, 7, 8, 9],
    [10, 21, 22, 23, 24, 25],
    [12, 7, 8, 9, 10, 11],
    [14, 8, 9, 10, 11, 12],
    [16, 9, 10, 11, 12, 13],
    [18, 10, 11, 12, 13, 14],
    [20, 27, 28, 24, 25, 26],
    [22, 12, 13, 14, 15, 16],
    [24, 13, 14, 15, 16, 17],
    [26, 14, 15, 16, 17, 18],
    [28, 15, 16, 17, 18, 19],
    [30, 29, 30, 31, 24, 25],
    [32, 17, 18, 19, 20, 32],
    [34, 18, 19, 20, 32, 32],
    [36, 19, 20, 32, 32, 32],
    [38, 20, 32, 32, 32, 32],
    [40, 32, 32, 32, 32, 32],
    [13, 22, 23, 24, 25, 26],
    [16, 23, 24, 25, 26, 20],
    [19, 24, 25, 26, 20, 32],
    [25, 25, 26, 20, 32, 32],
    [30, 26, 20, 32, 32, 32],
    [35, 20, 32, 32, 32, 32],
    [22, 28, 24, 25, 26, 20],
    [24, 24, 25, 26, 20, 32],
    [28, 30, 31, 24, 25, 26],
    [27, 31, 24, 25, 26, 20],
    [26, 24, 25, 26, 20, 32],
    [0, 32, 32, 32, 32, 32]
]

moves = list(map(int, input().split()))
answer = 0


def go(turn, result):
    global answer
    if turn == 10:
        answer = max(result, answer)
        return

    for i in range(4):
        move = moves[turn]
        cur_pos = pos[i]
        next_pos = board[cur_pos][move]

        if visited[next_pos] and next_pos != 32: continue

        add_score = board[next_pos][0]
        visited[next_pos] = 1
        visited[cur_pos] = 0
        pos[i] = next_pos
        go(turn+1, result + add_score)
        visited[next_pos] = 0
        visited[cur_pos] = 1
        pos[i] = cur_pos


visited = [0]*33
pos = [0, 0, 0, 0]

go(0, 0)
print(answer)