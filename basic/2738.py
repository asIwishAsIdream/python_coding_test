n, m = map(int, input().split(" "))

mylist1 = list(range(n))
mylist2 = list(range(n))
for i in range(n):
    mylist1[i] = list(map(int, input().split(" ")))

for i in range(n):
    mylist2[i] = list(map(int, input().split(" ")))

for i in range(n):
    if i > 0:
        print()
    for j in range(m):
        print(mylist1[i][j] + mylist2[i][j], end=" ")
