no = 105

ls = []
for i in range(0, no):
    for j in range(1, no + 1):
        if i * j == no:
            ls.append(i + j)

ls.sort()
print(f"Input  : {no}")
print(f"Output : {ls[0]}")
