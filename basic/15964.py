def help_sum(num1, num2):
    return (num1+num2)*(num1-num2)


numT1, numT2 = map(int, input().split(" "))
print(help_sum(numT1, numT2))
