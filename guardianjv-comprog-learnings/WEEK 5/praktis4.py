isPresent = False
isExist = True
isAvailable = True
isValid = 1
isOkay = 0
isNumeric = False
myChar = "5"
isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])

a = 6
b = 5
isEqual = (a == b)
print(isEqual)
isGTE = (a >=b)
print(isGTE)
isLTE = (a <=b)
print(isLTE)


isIn = (5 in [25, 45, 23, 12, 5, 27])
print(isIn)  # True
isIn = (5 in [25, 45, 23, 12, 27])
print(isIn)  # False
isIn = ("cute" in "cute ako")
print(isIn)  # True
isIS = ("cute" is "cute")
print(isIS)  # True
isIS = ("pogi" is "cute")
print(isIS)  # False


isOkay = (5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27])
print(isOkay)  # False

isOkay = (5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27])
print(isOkay)  # True


