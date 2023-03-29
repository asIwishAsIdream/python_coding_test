loop_flag = 1

while loop_flag:
    num_test1, num_test2 = map(int, input().split(" "))
    if num_test1 == 0 and num_test2 == 0:
        break
    print(num_test2 + num_test1)
