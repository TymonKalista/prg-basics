def compare(arr1,arr2):
    if len(arr1) != len(arr2):
        return 'arrays are different'
    for i in range(0,len(arr1)):
        if arr1[i] != arr2[i]:
            return 'arrays are different'
        else: 
            return 'arrays are the same'
tab1 = [True,False]  
tab2 = [True,False,True]
print(compare(tab1,tab2))