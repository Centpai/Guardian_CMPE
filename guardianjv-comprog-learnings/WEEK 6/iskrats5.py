myInfo = {"Name" : "Jan Vincent Guardian", "Age" : 19, "Gender" : "Male", "Address": "Kaligayahan"}
print(myInfo)
print(myInfo["Age"])
print(myInfo["Gender"])
print(myInfo["Address"])
print(myInfo["Name"])
print(myInfo.get("Name"))
myInfo["Name"] = "Daniel Padilla"
print(myInfo)
print(myInfo["Age"])
myInfo.update({"Gender": 4})
print(myInfo)

myInfo = {
    "Name":  {
        "FirstName ": "Daniel",
        "LastName": "Padilla",
    },
    "Age": 19,
    "Interest": [ "Mobile Legends", "Gym", "Eating" ]

}




print(myInfo)
print(myInfo["Name"]["FirstName "])
print(myInfo["Interest"])
print(myInfo["Age"])
print(myInfo["Name"]["FirstName "] + " " + myInfo ["Name"]["LastName"])
print(myInfo["Interest"][1])