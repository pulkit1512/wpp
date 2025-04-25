def magic_square(N):
    square = [[0] * N for _ in range(N)]
    i, j = 0, N // 2
    for num in range(1, N * N + 1):
        square[i][j] = num
        ni, nj = (i - 1) % N, (j + 1) % N
        if square[ni][nj] != 0:
            ni, nj = i + 1, j
        i, j = ni, nj
    return square

N = 5
for row in magic_square(N):
    print(row)
