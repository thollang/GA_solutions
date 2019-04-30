def find(list,aim,start=0,end=None):
    if end == None:
        end = len(list) - 1
    if start <= end:
        mid_index = (start + end)//2
        if list[mid_index] < aim:
            return find(list,aim,start=mid_index +1,end=end)
        elif list[mid_index] > aim:
            return find(list,aim,start=start,end=mid_index-1)
        else:
            return mid_index
    else:
        return 'cant found'

list=[1,3,5,6,9]
print(find(list,6))

