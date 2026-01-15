strFullname = "Jan Vincent Guardian"
strNewValue = strFullname.upper()
print(strNewValue)


strNewValue = strFullname.count ("a")
print(strNewValue)
strNewValue = strFullname.split(" ")
print(strNewValue)
strNewValue = strFullname.split("ua")
print(strNewValue)



strNewValue = strFullname.replace("Francie", "Fram")
print(strNewValue)


#join
strFirstName = "Jan Vincent"
strMiddleName = "Pogi"
strLastName = "Guardian"
strFullname = "Philippines".join([strFirstName, strMiddleName, strLastName])
print(strFullname)


newValue = strFullname.isnumeric()
print(newValue)


newValue = strFullname[2:10]
print(newValue)

newValue = strFullname[2:10:2]
print(newValue)

print(strFullname.index("e"))
print(strFullname.index("e", 2, 9 ))



