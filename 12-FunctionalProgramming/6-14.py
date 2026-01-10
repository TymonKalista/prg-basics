brew = [508,500,512,499,492,511,503,476,501,509]
incor = list(filter(lambda x: 500*0.98< x < 500*1.02, brew))
print(1-(len(incor)/len(brew)))