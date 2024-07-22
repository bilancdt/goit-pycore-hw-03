from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати без часу
        today = datetime.today().date()
        
        # Розрахунок різниці між поточною датою та заданою датою
        difference = input_date.date() - today
        
        # Повернення різниці у днях як ціле число
        return difference.days
    except ValueError:
        # Обробка винятків для неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."