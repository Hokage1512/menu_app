# ylab_menu_2023

### Настройка проекта
Клонируем приложение из репозитория и переходим в него
```bash
git clone https://github.com/Hokage1512/menu_app.git
cd menu_app
```

### Сборка образов и запуск контейнеров
В корне репозитория выполните команду:
```bash
docker-compose up --build -d
```

### Остановка контейнеров
Для остановки контейнеров выполните команду:
```bash
docker-compose stop
```
### Запускаем контейнер с приложением и тестовой базой данных
Для остановки контейнеров выполните команду:
```bash
docker-compose --file docker-compose.test.yml up --build -d
```
### Запускаем тестирование приложения
Для остановки контейнеров выполните команду:
```bash
docker-compose --file docker-compose.test.yml up app_test
```
### Останавливаем контейнер с приложением и тестовой базой данных
Для остановки контейнеров выполните команду:
```bash
docker-compose --file docker-compose.test.yml stop
```

Проект доступен по адресу http://127.0.0.1:8000/docs