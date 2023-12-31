# (a)
def list_splitting(lst, split_index):
    lst1 = []
    lst2 = []
    for i in range(len(lst)):
        if i < split_index:
            lst1.append(lst[i])
        else:
            lst2.append(lst[i])
    return lst1, lst2

values = [2, 4, 5, 1, 9] 
split_index = 3

lst1, lst2 = list_splitting(values, split_index)

print(values, lst1, lst2, sep="\n")

# (b)
def multiply(vals1, vals2):
    table = []
    for i in range(len(vals1)):
        row = []
        for j in range(len(vals2)):
            row.append(vals1[i] * vals2[j])
        table.append(row)
    return table

vals1 = [2, 5]
vals2 = [5, 6, 1]
print(multiply(vals1, vals2))