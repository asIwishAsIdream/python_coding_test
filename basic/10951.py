loop_flag = 1

while loop_flag:
    try:
        num_test1, num_test2 = map(int, input().split(" "))
        print(num_test2 + num_test1)
    except EOFError:
        break
