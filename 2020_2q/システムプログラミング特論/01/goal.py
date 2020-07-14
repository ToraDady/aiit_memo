def goal(count):
    if count > 9:
        s = 'Number of goals: many'
    else:
        s = 'Number of goals: ' + str(count)
    return s


print(goal(4))
print(goal(10))
