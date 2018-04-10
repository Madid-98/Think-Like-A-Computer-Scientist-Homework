milesDriven = input("How many miles have you driven?: ")
gallonsUsed = input("How many gallons have you used?: ")

milesDrivenInt = int(milesDriven)
gallonsUsedInt = int(gallonsUsed)

algo = milesDrivenInt / gallonsUsedInt

print("Your car's MPG is ", algo)