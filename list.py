# ages = [17, 18, 16, 16, 15, 17]
girls = ["petra","jess","amy","sophia","sophie","ali"]
girls[3] = "jullia"
print(girls)
print(girls[1])
print(girls[2:5])
# girls.extend(ages)
girls.append("bella")
girls.pop()
print(girls.index("sophie"))
girls.sort()
print(girls)
girls2 = girls.copy()
print(girls2)