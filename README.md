# api_yamdb
## Проект YaMDb собирает отзывы пользователей на произведения.
## Приложение работает через api
## Документацию проекта можно посмотреть по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Установка:
1. Проверить наличие Docker

Прежде чем приступать к работе, убедиться что Docker установлен, для этого ввести команду:
```
docker -v
```
В случае отсутствия, скачать Docker Desktop для Mac или Windows. Docker Compose будет установлен автоматически.

В Linux проверить, что установлена последняя версия Compose.

Также можно воспользоваться официальной инструкцией.

2. Клонировать репозиторий на локальный компьютер
```
git clone https://github.com/kichannf/infra_sp2.git
```

3. В корневой директории создать файл .env, согласно примеру:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres # Придумать свой
DB_HOST=db
DB_PORT=5432
```

4. Запустить ```docker-compose```
Выполнить из корневой директории команду:
```
docker-compose up -d
```
5. Заполнить БД

Создать и выполнить миграции:
```
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
```
6. Подгрузить статику
```
docker-compose exec web python manage.py collectstatic --no-input
```
7. Заполнить БД тестовыми данными

Создать дамп (резервную копию) базы:
```
docker-compose exec web python manage.py dumpdata > fixtures.json 
```
8. Создать суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
9. Остановить работу всех контейнеров
```
docker-compose down
```
10. Пересобрать и запустить контейнеры
```
docker-compose up -d --build
```
11. Мониторинг запущенных контейнеров
```
docker stats
```
12. Остановить и удалить контейнеры, тома и образы
```
docker-compose down -v
````