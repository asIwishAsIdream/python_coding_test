N, compareN = map(int, input().split(" "))

num_list = list(map(int, input().split()))

for n in range(N):
    if compareN > num_list[n]:
        print(num_list[n], end=" ")
