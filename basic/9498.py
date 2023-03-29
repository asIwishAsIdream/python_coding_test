while 1:
    st = int(input())
    if st <= 100 and st >= 0:
        break
if st >= 90:
    print("A")
elif st >= 80:
    print("B")
elif st >= 70:
    print("C")
elif st >= 60:
    print("D")
else:
    print("F")
