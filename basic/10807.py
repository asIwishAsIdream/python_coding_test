N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
cnt = 0

for n in range(N):
    if v == num_list[n]:
        cnt += 1
print(cnt)
