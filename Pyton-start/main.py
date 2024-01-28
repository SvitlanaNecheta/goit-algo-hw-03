import datetime as dt
import random
import re


def get_days_from_today(date):
    try:
        today_date = dt.datetime.today()
        print(f"Сьогодні {today_date}")
        delta = today_date.toordinal() - date.toordinal() 
        print(f"С {date} пройшло {delta} днів.")
    except TypeError:
        print("Введено некоректні данні")
 

date_str = "2020-10-19"   
date = dt.datetime.strptime(date_str,"%Y-%m-%d")

print("**********Завдання №1**********") 
get_days_from_today(date)

date_str=input('Введіть дату в форматі YYYY-MM-DD:')
date = dt.datetime.strptime(date_str,"%Y-%m-%d")
get_days_from_today(date)


#******************************************
def get_numbers_ticket(min, max, quantity):
    rezult_list = []
    i = 0 
    while (i<quantity):
        rezult_list.append(random.randint(min, max))
        i=i+1
    d_rezult=set(rezult_list)
    if len(d_rezult)>quantity:
        j=len(d_rezult)
        while j<quantity:
             j=j+1
             rezult_list.append(random.randint(min, max))
            
    rezult_list=list(d_rezult)     
    return f"{rezult_list}"

print("***********Завдання №2**********")    
print(get_numbers_ticket(1,49,6))
#******************************************
dirty_phons=[ "    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    p1=r"[\d\+]+"
    phone_number=''.join(re.findall(p1,phone_number))
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)==12:
        phone_number='+'+phone_number
    return phone_number

print("**********Завдання №3**********") 
for phone in dirty_phons:
    print(normalize_phone(phone))   
for phone in raw_numbers:
    print(normalize_phone(phone))   
#******************************************
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jak Smith", "birthday": "1990.01.30"},
]

def get_upcoming_birthdays(users=None):  
    td=dt.datetime.today().date()
    print(td)
    td.toordinal()
    birthdays=[]
    for user in users:
        b_date=user["birthday"]
        b_date=str(td.year)+b_date[4:]
        print(b_date)
        b_date=dt.datetime .strptime(b_date, "%Y.%m.%d").date()
        week_day=b_date.isoweekday()
        bdo=b_date.toordinal()
        days_between=td.toordinal()-bdo
        if -1<days_between<7:
            if week_day<6:
                birthdays.append({'name':user['name'], 'birthday':b_date.isoformat().replace('-','.')})
            else:
                if dt.datetime.fromordinal(bdo+1)==1:
                    birthdays.append({'name':user['name'], 'birthday':dt.datetime.fromordinal(bdo+1).isoformat.replace('-','.')})
                elif dt.datetime.fromordinal(bdo+2)==1:
                     birthdays.append({'name':user['name'], 'birthday':dt.datetime.fromordinal(bdo+2).isoformat.replace('-','.')})
        return birthdays
       

print("**********Завдання №4**********")
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))



 