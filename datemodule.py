from datetime import datetime

# The only required attributes inside the datetime is year month and day if they are not specified it will throw an error
dt = datetime(year=2022,month=5,day=10)
print(dt)

# Year start year to year till now, month 1 to 12, day 1 to 31(according to month),hour 0 to 23, minutes and seconds 0 to 59

dt1 = datetime(year=2022,month=5,day=10,hour=14,minute=59,second=59)
print(dt1)

# like this also we can go
dt2 = datetime(2022,5,10,14,59,59)
print(dt2)

