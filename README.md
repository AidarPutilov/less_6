## Домашняя работа 23.1
- Создана группа для роли модератора и опишисаны необходимые доступы.
-


### Применённые пакеты
- django
- ipython
- pillow
- psycopg2-binary
- django-crispy-forms
- crispy-bootstrap5

### Инструкция для развертывания проекта

#### Клонирование проекта:
```
git clone https://github.com/AidarPutilov/less_6.git
cd less_6
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