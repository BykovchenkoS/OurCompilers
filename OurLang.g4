grammar OurLang;

// начальное правило грамматики
program: (statement)* EOF;

statement: printStatement            // оператор печати
         | assignmentStatement       // оператор присваивания
         ;

// оператор печати
printStatement: 'print' expression ';' ;

// оператор присваивания
assignmentStatement: IDENTIFIER '=' expression ';' ;

// выражения с приоритетом и операциями
expression: expression op=(MUL | DIV) expression      # mulDivExpr
          | expression op=(PLUS | MINUS) expression   # addSubExpr
          | expression op=(AND | OR) expression       # logicalExpr
          | '!' expression                            # notExpr
          | '(' expression ')'                        # parenExpr
          | NUMBER                                    # numberExpr
          | IDENTIFIER                                # idExpr
          ;

// токены
IDENTIFIER       : [a-zA-Z_] [a-zA-Z_0-9]* ;  // идентификаторы (переменные)
NUMBER           : [0-9]+ ;                   // целые числа

// операторы
PLUS             : '+' ;
MINUS            : '-' ;
MUL              : '*' ;
DIV              : '/' ;
AND              : '&&' ;
OR               : '||' ;
NOT              : '!' ;

SPACE            : [ \r\n\t]+ -> skip;  // пропуск пробелов и переводов строк
