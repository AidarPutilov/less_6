## Домашняя работа 22.1
- Является продолжением работы 21.1.
- Реализован механизм CRUD для модели продуктов, использован модуль django.forms.
- Реализована валидация названия и описания продуктов.
- Добавлена модель "Версия".
- Реализован вывод в список продуктов информации об активной версии. Выводится последняя текущая версия.
- Добавлена реализация работы с формами для версий продукта с помощью пакета crispy-form.

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
git clone https://github.com/AidarPutilov/hm_19_2.git
cd hm_19_2
```
#### Первоначальные настройки:
- Ввести настройки сервера PostgreSQL в файле config.py.
- Создать базу данных les_20_1.
- Создать миграции, применить миграции.
- Заполнить БД командой
```
Windows: python manage.py fill
Linux, MacOS: python3 manage.py fill
```
- Задать логин и пароль администратора
```
Windows: python manage.py createsuperuser
Linux, MacOS: python3 manage.py createsuperuser
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
#### Административная страница:
```
http://127.0.0.1:8000/admin/
```
### Автор
Айдар Путилов