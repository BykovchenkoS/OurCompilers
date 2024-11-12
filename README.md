# OurCompilers
## docker:
build:
```docker build -t a:latest .```

run:
```docker run --rm -v ${PWD}:/dir -it a```

## in docker:
build: 
```antlr4 -Dlanguage=Python3 -o util -visitor OurLang.g4```

run: 
```python3 main.py```

---
## Задание
Разработать язык программирования, который должен реализовать следующие компоненты:

---
-[x] Присваивание (оператор или операция), арифметические и логические операции с возможностью изменения приоритета – скобочные формы;
-[x] Ветвление, включая вариант факультативного else;
-[ ] Цикл while;
-[ ] Поддержка целочисленного и логического типа данных; (Добавить логический)
-[x] Вывод значений переменных и констант;
-[x] Многострочные комментарии в стиле Си-подобных языков.

        /***********************************
        
        **** строки комментариев ************
        
        *************************************/

---
Что добавит баллы:
-[x] Вместо ветвление if [then] else конструируется оператор if elif [elif]+ else
-[ ] Вместо цикла while (или в дополнение к нему) конструируется цикл for
-[x] Реализуется вывод значений

Приветствуются:
- [x] Строки
- [ ] Введение в степень
- [ ] Остаток от деления


