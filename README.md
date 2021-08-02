# emphasoft_test_assignment
[![Build Status](https://www.travis-ci.com/fattybobcat/emphasoft_test_assignment.svg?token=xnqzf2HY5d6q74MCvyy9&branch=main)](https://www.travis-ci.com/fattybobcat/emphasoft_test_assignment)
[![codecov](https://codecov.io/gh/fattybobcat/emphasoft_test_assignment/branch/main/graph/badge.svg?token=Ue7yTp55cD)](https://codecov.io/gh/fattybobcat/emphasoft_test_assignment)

Test Task for emphasoft

### Установка

Клонируйте репозиторий с проектом https://github.com/fattybobcat/emphasoft_test_assignment.git

Создайте виртуальное пространство python -m venv venv и активируйте его.

Установите необходимые модули pip install -r requirements.txt

## Работа с проектом
Примените миграции `python manage.py migrate`

Создайте superuser  `python manage.py createsuperuser`

Запустите проект `python manage.py runserver`

### Запустите Postman
Получите авторизацию superuser: 
`GET http://127.0.0.1:8008/api-token-auth/`
с логином и паролем вашего superuser
```
username: admin
password: password
```
Используя полученный токен, согласно документации на [API](https://emphasoft-test-assignment.herokuapp.com/swagger/) можете посылая запросы создавать новых user, изменять их данные и удалять

## Aвтор проекта

Петрук Александр - [GitHub](https://github.com/fattybobcat)

[резюме](https://github.com/fattybobcat/emphasoft_test_assignment/blob/main/cv_Petruk.pdf)

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)