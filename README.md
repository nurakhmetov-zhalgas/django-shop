# Django E-commerce Shop
## Реализована backend составляющая и настройка контейнеров. В качестве Frontend части использованы Django шаблоны

### Функционал
- Корзина товаров на основе сессии
- Добавлен Stipe в качестве платежного шлюза + webhook для обработки ответов от Stripe о статусе платежа
- Celery задачи (в качестве брокера сообщения используется RabbitMQ) на отправку подтверждения заказа, а также генерация PDF счет-фактур(отправляется так же на почту)
- Настройка Админ панели Django (кастомные страницы, реализована возможность генерации csv отсчетов из админ части)
- Простая рекомендательная система на основе купленных вместе товаров, реализована на key-value хранилище (Redis) 

### Технологии
- Python
- Django
- Docker
- PostgreSQL
- Celery
- Redis
- RabbitMQ
- StripeAPI

# Как запустить приложение

1) Клонируйте репозиторий
```shell
git clone https://github.com/nurakhmetov-zhalgas/django-shop.git
```
2) Поставьте виртуальное окруженин и установите зависимости
```shell
cd Food-app
python3 -m venv venv
source venv/bin/activate # в зависимости от ОС
pip install -r backend/requirements.txt
```
3) Создайте в корне проекта файл .env (на примере файла .env.example)
```shell
mv ./env.example ./env
```
5) Запустите сборку контейнеров. Необходимо заранее установить docker, docker-compose
```shell
sudo docker-compose up --build
```
Проект развернут на localhost

Чтобы получить доступ в админку необходимо создать суперпользователя
```shell
sudo docker-compose exec web python manage.py cretesuperuser
```

