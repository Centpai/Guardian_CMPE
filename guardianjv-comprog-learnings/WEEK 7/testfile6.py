originalValue = "Lakers"

print("originalValue = " + originalValue)
newValue = ""

for x in originalValue:
    newValue = x + newValue

print("newValue = " + newValue)

print(originalValue[::-1])


print("before loop")

for i in range(10):

    if i % 2 == 0:
        print("Even number = " + str(i))
        continue

    if i > 6:
        print("i is greater than 6")
        break


print("i value is : " + str(i))
print("after loop")
