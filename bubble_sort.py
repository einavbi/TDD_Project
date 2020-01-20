def check(lst):
    size=len(lst)
    i=0
    while(i!=(size-1)):
        if(lst[i]<lst[i+1]):
            i=i+1
        else:
            return False
    return True


def bubblesort(lst):
    "Sorts lst in place and returns it."
    size=len(lst)
    if len(lst)==0:
        return "no input"
    for passesLeft in range(len(lst) - 1, 0, -1):
        for index in range(passesLeft):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    if(size!=len(lst)):
        return "the array lost value"
    if(check(lst)==False):
        return "List not Sorted"
    else:
      return lst

