# **Сервис Транзакции**

Тестовый проект для пользовательских транзакций.

Стек:
- `FastAPI`
- `PostgreSQL`
- `SQLAlchemy`
- `Docker`
- `docker-compose`

## **Краткое описание работы микросервиса**
После развертывания сервис принимает POST запросы для регистрации и авторизации клиентов, 
после чего можно отправлять GET запросы на пополнение или снятие суммы со счета, либо на
отображение баланса.

## **Локальное развертывание**

Для локального развертывания необходим Docker и docker-compose.

После установки docker, docker-compose ввести команду:

    docker-compose up --build

Теперь можно перейти в папку docs, где лежат примеры http запросов, либо воспользоваться 
HTTP клиентом, например Postman.

POST запрос для регистрации клиента:
http://localhost:8000/register

Тело запроса:
{
  "email": str,
  "name": str,
  "psw": str,
  "psw_repeat": str
}

POST запрос для авторизации клиента:
http://localhost:8000/login

Тело запроса:
{
  "email": str,
  "psw": str
}

GET запрос для пополнения счета:
http://localhost:8000/increase?amount=int

GET запрос для снятия со счета:
http://localhost:8000/decrease?amount=int

GET запрос для отображения баланса:
http://localhost:8000/balance
