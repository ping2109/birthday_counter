from datetime import date 
from datetime import timedelta
from datetime import datetime

BIRTH_DAY = 21
BIRTH_MONTH = 9

current_year = str(datetime.now().year)
next_year = str(datetime.now().year + 1)


current_birthday = BIRTH_DAY + "/" + BIRTH_MONTH + "/" + current_year 
next_birthday = BIRTH_DAY + "/" + BIRTH_MONTH + "/" + next_year

current_bd_date = datetime.strptime(current_birthday, '%d/%m/%Y')
next_bd_date = datetime.strptime(next_birthday, '%d/%m/%Y')
current_date = datetime.now()


if current_bd_date < current_date :
	print(str(next_bd_date - current_date) + " until your birthday.")
else:
    print(str(current_bd_date - current_date) + " until your birthday.")
