# Копирование проекта на локальный компьютер

1. Создать новый проект в PyCharm.

Команды ниже необходимо вводить через терминал PyCharm<br>

2. Склонировать проект в PyCharm: <br>
`git clone https://github.com/Olga-Yar/test_dash`
3. Нажать Enter
5. Установть виртуальное окружение:<br>
`python3 -m venv venv`
6. Активировать виртуальное окружение:<br>
`source venv/bin/activate` # macOS, Linux<br>
`venv\Scripts\activate` # Windows
7. В терминале в начале строки должно появиться "(venv)"
8. Должна появиться папка venv<br><br>

9. Установить все зависимости<br>
`pip3 install -r requirements.txt`
10. Запустить приложение. Основной файл main.py - run.

При успешном запуске в терминале появится:
```
...
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'main'
 * Debug mode: on
 ...
```

11. Нужно нажать на ссылку или скопировать ее в браузер для запуска приложения на localhost
```http://127.0.0.1:8050/```


**При работе на Windows вместо python3 и pip3 необходимо использовать python и pip.**

---
12. Обновление проекта локально<br>
В терминале в Pycharm написать команду:<br>
`git pull origin main`<br>

'main' - название вашей локальной ветки, если название 
другое - замените на то, которое указано в вас.

13. Выполнить команду для обновления зависимостей:<br>
`pip3 install -r requirements.txt`
