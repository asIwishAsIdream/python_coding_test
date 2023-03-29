sum = 0
my_list = []
my_list = list(map(int, input().split(" ")))
for i in my_list:
    sum = sum + i**2

print(sum % 10)
