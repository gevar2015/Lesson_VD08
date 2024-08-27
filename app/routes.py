import requests
from flask import render_template
from app import app

@app.route('/')
def home():
    # Делаем запрос к API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random')

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Получаем данные цитаты в формате JSON
        data = response.json()
        quote = data.get('content')
        author = data.get('author')
    else:
        # Если запрос не удался, устанавливаем цитату и автора по умолчанию
        quote = "Sorry, couldn't fetch a quote at this moment."
        author = "Unknown"

    # Рендерим шаблон, передавая данные цитаты
    return render_template('quote.html', quote=quote, author=author)
