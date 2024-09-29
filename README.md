## Домашняя работа 23.1
- Создана группа для роли модератора.
- Описаны доступы для модели Product: 'can_edit_in_stock' - изменение наличия продукта (публикация по условию задачи), 'can_edit_description' - изменение описания продукта, 'can_edit_category' - изменение категории продукта.
- Функция csu модифицирована для создания 3х пользователей: admin@sky.pro - администратор, user1@sky.pro - с правами модератора, user2@sky.pro - обычный пользователь. Пароль у всех: 123qwe.
- Группы сохранены в фикстуре groups.json.
- Создана форма ProductModeratorForm для доступа модератору.
- Реализовано условие доступа редактирования модератору.
- Реализована проверка владельца в шаблоне. Кнопки редактирования доступны при наличии разрешений.

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