Как установить зависимости
--------------------------

В консоли выполняем команду:
```bash
pip3 install -r requirements.txt
```

Как запустить тесты
-------------------

В линуксе из главной дирректории проекта выполняем команду:
```bash
python3 -m pytest -v --driver Chrome --driver-path ~/chrome -x
```
B Windows из главной дирректории проекта выполняем команду:
```bash
python -m pytest -v --driver Chrome --driver-path C:/Windows/chromedriver.exe
```
