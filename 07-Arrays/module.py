import statistics
def second_max(array):
    unique_vals = list(set(arr))     # remove duplicates
    unique_vals.sort(reverse=True)   # sort descending
    return unique_vals[1]
def difference(array):
    return max(array) - min(array)
def median(array):
    return statistics.median(array)
def smallest_and_largest(array):
    new_arr = [min(array), max(array)]
    return new_arr
def string(array):
    return ("-".join((str(x) for x in array)))

arr = [7,3,8,5,2]
print(second_max(arr))
print(difference(arr))
print(median(arr))
print(smallest_and_largest(arr))
print(string(arr))
