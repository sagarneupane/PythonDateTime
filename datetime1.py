
from time import time,ctime,localtime


epoch = time()
print(epoch)

# The ctime module in datetime will provide you the seconds conversion into datetime. 
mytime = 1645545555.2545
if mytime <= epoch:
    et = ctime(mytime)
    print(et)
else:
    print("Your Time exceeds current Datetime")


ltobj = localtime()
print(ltobj)
print(ltobj.tm_hour)
