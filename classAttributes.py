# In this piece of code we are learning to access the datetime class attributes


from datetime import datetime


datetoday = datetime.today()

print("The year today is",datetoday.year)
print("The month today is",datetoday.month)
print("The day today is",datetoday.day)
print("The hour now is",datetoday.hour)
print("The minute now is",datetoday.minute)
print("The second now is",datetoday.second)
print("The microsecond now is",datetoday.microsecond)