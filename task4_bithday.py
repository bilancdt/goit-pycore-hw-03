from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримання поточної дати
    today = datetime.today().date()
    # Список для збереження результатів
    upcoming_birthdays = []

    for user in users:
        # Конвертація дати народження з рядка у datetime об'єкт
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Заміна року народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже пройшов у цьому році, взяти дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Розрахунок різниці між поточною датою та днем народження
        days_until_birthday = (birthday_this_year - today).days

        # Перевірка, чи день народження настає протягом наступних 7 днів
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження випадає на вихідний, перенести привітання на наступний робочий день (понеділок)
            if birthday_this_year.weekday() >= 5:  # субота = 5, неділя = 6
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            # Додавання інформації до списку результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1985.07.20"},
    {"name": "Bob Brown", "birthday": "1992.07.24"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
