def binary(list, item):
    first = 0
    last = len(list)-1
    found = False
    while first <= last and not found:
        mid = (first+last) // 2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

def binaryRecursive(list, item):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == item:
            return True
        else:
            if item < list[mid]:
                return binaryRecursive(list[:mid], item)
            else:
                return binaryRecursive(list[mid:], item)

def sequentialSearch(list, item):
    pos = 0
    found = False
    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos += 1
    return found