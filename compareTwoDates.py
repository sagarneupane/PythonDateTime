# Comparison Operators in Python Datetime

from datetime import datetime

d1 = datetime(2019,12,20)
d2 = datetime(2019,11,25)
d3 =  datetime(2020,10,1)
d4 = datetime(2020,10,1)

print("Is Date1 greater than date2? ",d1>d2)
print("Is Date1 smaller than date2? ",d1<d2)
print("Is Date1 smaller than date3? ",d1<d3)
print("Is Date3 smaller than date1? ",d3<d1)
print("Is Date4 same as Date3? ", d4==d3)