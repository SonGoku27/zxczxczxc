zxc, N, R, C = 0, int(input()), int(input()), int(input())
for i in range(1, N + 1):
    zxc = zxc + sum([R + i <= N and C + i <= N, R + i <= N and C - i > 0, R - i > 0 and C - i > 0,
                     R - i > 0 and C + i <= N])
print(zxc)


N, R, C = int(input()), int(input()), int(input())
print(min(R - 1, C - 1) + min(R - 1, N - C) + min(N - R, C - 1) + min(N - R, N - C))