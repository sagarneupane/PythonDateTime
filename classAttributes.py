# In this piece of code we are learning to access the datetime class attributes


from datetime import datetime

# The today() method of the datetime class gives current time but doesnot take the time zone attribute
# We have another method now() also which gives current time but takes time zone attributes as well if timezone is not passed into that method it 
# -- will acts same as tody() --
# let's go on with today in this section
datetoday = datetime.today()

print("The year today is",datetoday.year)
print("The month today is",datetoday.month)
print("The day today is",datetoday.day)
print("The hour now is",datetoday.hour)
print("The minute now is",datetoday.minute)
print("The second now is",datetoday.second)
print("The microsecond now is",datetoday.microsecond)