Lab_3: Вступ до моніторингу.
-
1. Створюю папку з назвою лабораторної роботи у власному репозиторію. У папці ініціалізовую середовище pipenv командою `pipenv -python 3.7` та встановлюю необхідні пакети за допомогою команди `pipenv install django`.
2. За допомогою Django Framework створюю заготовку проекту командою `pipenv run django-admin startproject vsite`. Для зручності виношу всі створені файли на один рівень вище. У результаті получається наступна структура:  
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/1.png)
3. Оскільки все встановлено правильно, то запускаю Django сервер, виконавши команду `pipenv run python manage.py runserver`. Переходжу за посиланням `localhost:8000`:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_3/img/2.png)