# Проект "Rochwin test"

Данный проект представляет собой реализацию тестового задания для Backend Разработчиков.

## Требования

- Python 3.9
- Docker

## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Sniperat/Rochwin_test.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd Rochwin_test
    ```
3. Создайте файл `.env`
    ```
    SECRET_KEY=django-insecure-@%*3b8xkb)1fbjaxf*^olgbx%n26eqr0%)zmk9q(&h0@09lwxn
    DEBUG=True
    ALLOWED_HOSTS=*
    DATABASE_URL=psql://postgres:postgres@db:5432/postgres
    ```
4. Запустите Docker Compose для создания и запуска контейнеров:

    ```bash
    docker-compose up --build
    ```

5. После успешного запуска, проект будет доступен по адресу `http://localhost:8000`.


## Коротко о проекте

на техническом задании не было описано про масштаб этого проекта. поэтому я использовал шаблона проектирования MVC (Model-View-Controller). Вот краткое описание каждой из частей:

- **Модель (Model)**: Отвечает за обработку и хранение данных приложения. В данном проекте модель представлена классами (каждый из них отдельный аpplication), описывающими сущности базы данных (например, `Employee`, `Client`, `Product`, `Order`).

- **Представление (View)**: Отвечает за отображение данных пользователю. В нашем проекте это представлено как виевс и API эндпоинтами.

- **Контроллер (Controller)**: Отвечает за обработку запросов пользователя и взаимодействие между моделью и представлением. обычно сама конструкция Джанго не подходит для такого масштабного проекта. я всю бизнес логику переместил на контроллер (`service.py`). больше информации [здесь](https://habr.com/ru/companies/vivid_money/articles/544856/)


Ещё дополнительно я добавил [pre-commit](https://pre-commit.com/) это библиотека перед коммитами помогает проверять коды на соответствие различным стандартам которую вы сами назначайте.
и ещё сваггер😉 После запуска проекта, вы можете открыть интерфейс Swagger для документации и тестирования API, перейдя по адресу `http://localhost:8000/swagger`.

## Описание ТЗ

Азиз – предприниматель, владелец собственного бизнеса по продаже медтехники. Его компания имеет множество сотрудников, и он, как заботливый руководитель, стремится поощрять лучших из них. Кроме того, он желает иметь возможность отслеживать производительность каждого сотрудника и анализировать статистику продаж. В настоящее время он ведет все расчеты вручную. Статистика сотрудника должна включать:

    Количество проданных товаров
    Количество уникальных клиентов
    Общая сумма продаж

Требуется вывести статистику за определенный период. В статистику клиента должны входить:

    Количество купленных товаров
    Общая сумма продаж

Ваша задача состоит в разработке REST API с использованием Django Rest Framework (DRF), которое сможет:

• Подсчитывать статистику для отдельного сотрудника
• Подсчитывать статистику для всех сотрудников
• Подсчитывать статистику для отдельного клиента

Требования:

• Django Rest Framework (DRF)
• Docker
• База данных на ваше усмотрение (рекомендуется использовать Postgres)

Задачу необходимо выполнить в течение 3 дней с момента получения. Пожалуйста, отправьте ссылку на репозиторий GitHub в качестве ответа.

Техническое задание:

    Метод GET /statistics/employee/{id}/?month=1&year=2023 возвращает – ФИО, количество клиентов, количество товаров, сумму продаж
    Метод GET /employee/statistics/?month=1&year=2023 возвращает – id сотрудника, ФИО, количество клиентов, количество товаров, сумму продаж
    Метод GET /statistics/client/{id}?month=1&year=2023 возвращает – id клиента, ФИО, количество купленных товаров, сумму продаж

Сущности для использования:

Employee (сотрудник):

    full_name – ФИО
    birthdate – дата рождения

Client (клиент):

    full_name - ФИО​
    birthdate – дата рождения

Product (продукт):

    name - имя продукта
    quantity - количество в наличии
    price - цена

Order (заказ):

    client – клиент
    products – продукты (может содержать несколько товаров в заказе)
    employee – сотрудник
    price – общая цена заказа
    date - дата заказа
