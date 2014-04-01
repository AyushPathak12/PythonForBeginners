a,b = 1,1

if a == 1 and b == 1:
    print(1)
elif (a == 0 and b == 0) or (a == 1 and b == 0) or (a == 0 and b == 1):
    print(0)
else:
    print("Invalid Input")

if a == 1 or b == 1:
    print(True)
elif a == 0 or b == 0:
    print(False)
elif a == 1 or b == 0:
    print(True)
elif a == 0 or b == 1:
    print(True)