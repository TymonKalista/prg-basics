test_scrs = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return list(filter(lambda pts: pts>=limit, test_scrs))
print(min_pts(50))

