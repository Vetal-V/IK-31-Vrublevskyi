Lab_2: Автоматизація. Знайомство з CI/CD.
-

1. Створюю папку lab_2 з README.md файлом. 
2. За допомогою пакетного менеджера PIP інсталюю pipenv за допомогою команди `pip install pipenv` та створюю ізольоване середовище командою `pipenv --python 3.7`. Запускаю середовище командою `pipenv shell`.
3. У ізольованому середовищі встановлюю бібліотеки requests і ntplib командами `pipenv install requests` та `pipenv install ntplib`. 
4. Створюю файл app.py і копіюю код програи із репозиторію до себе.
5. В ізольованому середовищі запускаю програму командою `python app.py`. Програма працює правильно.
6. Встановлюю бібліотеку pytest за допомогою команди `pipenv install pytest`.
7. Копіюю приклади тестів та виконую їх командою `pytest tests/tests.py`. Тести виконалися успішно.
8. Дописую функцію, яка перевіряє час доби AM/PM та відповідно друкує Доброго дня/ночі:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_2/img/img1.png)

9. Пишу тест для перевірки правильності виконання функції:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_2/img/img2.png)
10. Перенаправляю результат виконання тестів у файл result.txt та результат виконання програми у кінець цього ж файлу за допомогою команд `pytest tests/tests.py > results.txt` та `python app.py >> results.txt`.
11. Роблю коміт зі всіма змінами в репозиторій.
12. Заповнюю Makefile необхідними командами для повної автоматизації процесу СІ проекту.
13. Комічу зміни в Makefile до репозиторію та переходжу на віртуальну машину Ubuntu.
14. Клоную git репозиторій на віртуальну машину та запускаю Makefile:
![image](https://github.com/Vetal-V/IK-31-Vrublevskyi/blob/master/lab_2/img/img3.png)
