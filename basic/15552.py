import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    num_test1, num_test2 = map(int, sys.stdin.readline().split(" "))
    print(num_test1 + num_test2)
