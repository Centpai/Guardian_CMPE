TeamA = {"Kalbo", "Panot", "Shaggy","Urot"}
TeamB = {"Pilay", "Bulag","Bingi","Banlag"}
print(TeamA)
TeamA.add("audi")
print(TeamA)


TeamsUnion = TeamA.union(TeamB)
print(TeamsUnion)
TeamsIntersection = TeamA.intersection(TeamB)
print(TeamsIntersection)
TeamDifference = TeamA.difference(TeamB)
print(TeamDifference)

