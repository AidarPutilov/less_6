## Домашняя работа 23.2
- Установлен и настроен брокер для кеширования. Использовался WSL Linux.
- Реализовано кеширование контроллера отображения данных относительно одного продукта в файле маршрутизации.
- Реализованы контроллер и шаблон списка категорий.
- Создана сервисная функция, которая будет отвечает за выборку категорий. Добавлено низкоуровневое кеширование для списка категорий.
- Настройки перенесены в переменные окружения. Проект модифицирован для работы с ними.

### Применённые пакеты
- django
- ipython
- pillow
- psycopg2-binary
- django-crispy-forms
- crispy-bootstrap5
- redis
- python-dotenv

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/less_6.git
cd less_6
poetry shell
poetry install
```
#### Первоначальные настройки:
- Ввести настройки сервера PostgreSQL в файле config.py.
- Создать базу данных les_20_1.
- Применить миграции.
- Заполнить БД командой
```
Windows: python manage.py fill
Linux, MacOS: python3 manage.py fill
```
#### Добавление пользователей:
- Выполнить команду:
```
Windows: python manage.py csu
Linux, MacOS: python3 manage.py csu
```
#### Заполнить права доступа:
- Выполнить команду:
```
Windows: python manage.py loaddata groups.json
Linux, MacOS: python3 manage.py loaddata groups.json
```
#### Запуск сервера:
```
Windows: python manage.py runserver
Linux, MacOS: python3 manage.py runserver
```
#### Запуск страницы:
```
http://127.0.0.1:8000/
```
### Автор
Айдар Путилов