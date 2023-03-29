popular_num1, popular_num2 = map(int, input().split(" "))

sum_num = popular_num1 - popular_num2

if sum_num < 0:
    sum_num = sum_num * -1

print(sum_num)
