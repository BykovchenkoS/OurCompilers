# OurCompilers
## docker:
build:
```docker build -t a:latest .```

run:
```docker run --rm -v ${PWD}:/dir -it a```

## in docker:
build: 
```antlr4 -Dlanguage=Python3 -o util -listener -visitor OurLang.g4```

run: 
```python3 main.py```