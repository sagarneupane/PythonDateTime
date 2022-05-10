from datetime import timedelta,datetime,date

myTime = datetime.now()
# myDate = myTime.strftime("%y-%m-%d")
myDate = date.today()
print("Date Today",myDate)
td1 = timedelta(days=10)
print("Date after 10 days",myDate + td1)



timeonly = myTime.strftime("%H:%M:%S")
print("Time Now is : ",timeonly)
td2 = timedelta(hours=1)

timeInc = myTime + td2
print("Time After 1 hour increment is : ",timeInc.strftime("%H:%M:%S"))
timeDec = myTime - td2

print("Time After 1 hour decrement is : ", timeDec.strftime("%H:%M:%S"))

