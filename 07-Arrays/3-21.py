ar1 = [1,2,5]
ar2 = [1,2,3,4]
def is_subset(arr1,arr2):
    if len(arr1)>len(arr2):
        return False
    for i in arr1:
        if i not in arr2:
            return False
    return True
print(is_subset(ar1,ar2))
