# Проект YaMDb
## Описание проекта
Проект собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти.

## Установка:
1. Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:mtedoradze/api_yamdb.git`
2. Cоздать и активировать виртуальное окружение:
`python3 -m venv env`
`source env/bin/activate`
3. Установить зависимости из файла requirements.txt:
`python3 -m pip install --upgrade pip`
`pip install -r requirements.txt`
4. Выполнить миграции:
`python3 manage.py migrate`
5. Запустить проект:
`python3 manage.py runserver`

## Примеры запросов:
См. документацию по проекту: http://localhost/redoc/
