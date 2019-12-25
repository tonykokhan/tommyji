import time

b = int(time.time())
print(b)

totalMinutes = b/60
print(totalMinutes)

totalMinutes = b//60
print(totalMinutes)

totalHours = totalMinutes//60
print(totalHours)

totalDays = totalHours//24
print(totalDays)

totalYears = totalDays//365
print(totalYears)
