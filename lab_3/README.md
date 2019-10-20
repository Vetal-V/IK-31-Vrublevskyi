Lab_3: Вступ до моніторингу.
-
1. Створюю папку з назвою лабораторної роботи у власному репозиторію. У папці ініціалізовую середовище pipenv командою `pipenv -python 3.7` та встановлюю необхідні пакети за допомогою команди `pipenv install django`.
2. За допомогою Django Framework створюю заготовку проекту командою `pipenv run django-admin startproject vsite`. Для зручності виношу всі створені файли на один рівень вище. У результаті получається наступна структура:  
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/1.png)

3. Оскільки все встановлено правильно, то запускаю Django сервер, виконавши команду `pipenv run python manage.py runserver`. Переходжу за посиланням `localhost:8000`:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/2.png)

4. Зупиняю сервер виконавши переривання `Ctrl+C`. Роблю коміт базового темплейту сайту.
5. Створюю темплейт додатку (app), у якому буде описано всі web сторінки сайту за допомогою команди `pipenv run python manage.py startapp main`. Роблю коміт із новоствореними файлами темплейту додатка.
6. Використовуючи можливості IntelliJ створюю папку `main/templates/`, файл `main.html` у цій папці та файл `urls.py`. Роблю коміт з даними файлами.
7. Вказую Django frameworks назву додатку та де шукати його веб-сторінки у файлах `vsite/setting.py` та `vsite/url.py` відповідно.
8. Заповнюю вміст файлу `main/urls.py` для відображення `.html` темплейта та сторінки, що повертає відповідь у форматі JSON.
9. Заповнюю файл `main/urls.py` згідно зразка, щоб поєднати функції з реальними URL шляхами, за якими будуть доступны веб-сторінки.
10. Запускаю сервер, щоб переконатися, що сторінки доступні:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/3.png)

![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/4.png)
Виконую коміт робочого Django сайту.