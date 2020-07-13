def remove_adjacent(li):
    tmp = []
    last_num = 0
    for i in li:
        if last_num != i:
            tmp.append(i)
            last_num = i
    return tmp


print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([]))
