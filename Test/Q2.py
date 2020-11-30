a = "apple banana mango"
b = "banana fruits mango"
ls = []

a1 = a.split()
b1 = b.split()

for i in a1:
    if i not in a1[a1.index(i) + 1:]:
        if i not in b1:
            ls.append(i)
for i in b1:
    if i not in b1[b1.index(i) + 1:]:
        if i not in a1:
            ls.append(i)

print(ls)
