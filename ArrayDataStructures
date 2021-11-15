reactorTypes = ["PWR", "BWR", "GFR", "LFR"]

numberOfUnits = (1, 2, 3)

powerLevel = {"Low" : 200, "Medium" : 600, "High" : 1200}


# Changing a list is possible
print(reactorTypes)
reactorTypes[1] = "SFR"
print(reactorTypes)
print()

# Changing a tuple will generate an error
#numberOfUnits[2] = 4

# Accessing a new item in a dictionary will add it to the dictionary
print(powerLevel)
powerLevel["Very High"] = 1500
print(powerLevel)
print()

selectedReactor = reactorTypes[0]
selectedUnits = numberOfUnits[2]
selectedPower = powerLevel["Medium"]

print(f"I want to build {selectedUnits} {selectedReactor} units, each at a power level of {selectedPower} MW")
