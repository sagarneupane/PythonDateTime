from datetime import datetime

datenow = datetime.now()
# datenow = datetime.today()

print("Full Week Day",datenow.strftime("%A"))
print("Short week day",datenow.strftime("%a"))
print("Week Day number",datenow.strftime("%w"))
print("Month Name Short",datenow.strftime("%b"))
print("Month Name Full",datenow.strftime("%B"))
print("Year Short Version",datenow.strftime("%y"))
print("Year long Version",datenow.strftime("%Y"))
print("Hour 24 format",datenow.strftime("%H"))
print("Hour 12 format",datenow.strftime("%I"))
print("Local Version of Date and Time",datenow.strftime("%c"))
print("Week Number of the year Sunday as Day First ",datenow.strftime("%U"))
print("Week Number of the year Monday as Day First ",datenow.strftime("%W"))
print("Day number of the year ",datenow.strftime("%j"))
print("Time Zone",datenow.strftime("%Z"))
print("AM or PM in 12 hrs format::",datenow.strftime("%p"))
print("Local Version Of date",datenow.strftime("%x"))
print("Local Version Of time:",datenow.strftime("%X"))

# print(datenow.tzinfo)