no = 15
ls = []

for i in range(2, no):
    for j in range(3, no + 1):
        if i * j == no:
            if i > 1:
                for k in range(2, no//2):
                    if i % k != 0:
                        ls.append(i)
            if j > 1:
                for k in range(2, no//2):
                    if j % k != 0:
                        ls.append(j)
            if i == 2 or j == 2:
                ls.append(2)


ls.sort()
print(ls[ls.__len__()-1])
