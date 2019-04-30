def count(list):
    if list == []:
        return 0
    else:
        return 1+count(list[1:])

print(count([2,5,3,2,6,7,2,1,5,6]))
