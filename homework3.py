from datetime import date, datetime
def calculate_age(birthdate):
   try:
    day, month, year = map(int, birthdate.split('/'))
    birthdate = date(year, month, day)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
   except ValueError:
    return "Некорректный формат даты рождения. Введите дату в формате ДД/ММ/ГГГГ."
birthdate_str = input("Введите дату рождения в формате ДД/ММ/ГГГГ: ")
age = calculate_age(birthdate_str)
print("Ваш возраст:",age,"лет")

