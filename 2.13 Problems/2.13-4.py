startingDay = input("Starting day of the week: ")
stayLength = input("Length of stay: ")

startingDayInt = int(startingDay)
stayLengthInt = int(stayLength)

print("Holiday started on day ", startingDayInt, " and they stayed for ", stayLengthInt, " days")

returnDay = (startingDayInt + stayLengthInt) % 7

print("They came back on day ", returnDay)
