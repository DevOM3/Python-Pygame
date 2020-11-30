# inp = int(input("Enter an even number :- "))
inp = 4

row = int(input("Enter max star to be display on single line "))
rows = row + 1
for i in range(0, rows):
    for j in range(0, i + 1):
        if j % 2 == 0:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        if j % 2 == 0:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print("\r")
