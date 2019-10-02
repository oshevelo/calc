# Разница между датами в днях:
import datetime
today = datetime.datetime.now()
print("Date today :", today)
print()

def difference_date():
    first_date = input("First date (yyyy-mm-dd): ")
    second_date = input("Second date (yyyy-mm-dd): ")

    date1 = first_date.split('-')
    date2 = second_date.split('-')

    date_first = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    date_second = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))

    operation = date_first - date_second
    return operation

result = difference_date()
print("Difference of day :", result)


# +/- от указанной даты
import datetime
def day_date():

    date = input("First date (yyyy-mm-dd): ")
    date1 = date.split('-')
    date_first = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))

    day = input("Enter day +/- :")
    day = int(day)
    days = datetime.timedelta(days=day)

    operation = date_first + days
    return operation

result = day_date()
print("Difference of day :", result)