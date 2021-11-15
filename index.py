import datetime

with open('Student.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
for row in rows:
   str = row.split(",")
   age = str[3]
   now = datetime.datetime.now()
   print(row,age)