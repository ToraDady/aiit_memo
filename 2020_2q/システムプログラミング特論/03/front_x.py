# coding: utf-8

def front_x(x):
    x_list = []
    non_x_list = []
    for i in x:
        if i[0] == 'x':
            x_list.append(i)
        else:
            non_x_list.append(i)

    x_list.sort()
    non_x_list.sort()

    return x_list + non_x_list


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
