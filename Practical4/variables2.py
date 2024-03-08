#   X     Y     either X or Y
# True   True      False
# True   False     True
# False  True      True
# False  False     False
X=input("X=")
Y=input("Y=")
if X!=Y:
    W=True
else:
    W=False
print(f"W={W}")