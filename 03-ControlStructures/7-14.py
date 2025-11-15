facebook = True
twitter = False
instagram = True
if (facebook and twitter) or (twitter and instagram) or (instagram and facebook):
    print("You are a good influencer")
else:
    print("You are a bad influencer")