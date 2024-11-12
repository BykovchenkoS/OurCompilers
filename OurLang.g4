grammar OurLang;

// начальное правило грамматики
program: (statement)* EOF;

statement: printStatement            // оператор печати
         | assignmentStatement       // оператор присваивания
         | ifStatement              // оператор ветвления
         ;

// оператор печати
printStatement: 'print' expression ';' ;

// оператор присваивания
assignmentStatement: IDENTIFIER '=' expression ';' ;

// ветвление if-elif-else
ifStatement
    : 'if' '(' expression ')' '{' statement* '}' (elifStatement)* (elseStatement)?
    ;

elifStatement
    : 'elif' '(' expression ')' '{' statement* '}'
    ;

elseStatement
    : 'else' '{' statement* '}'
    ;

// выражения с приоритетом и операциями
expression: expression op=(MUL | DIV) expression      # mulDivExpr
          | expression op=(PLUS | MINUS) expression   # addSubExpr
          | expression op=(GT | LT | GE | LE | EQ | NEQ) expression # comparisonExpr
          | expression op=(AND | OR) expression       # logicalExpr
          | '!' expression                            # notExpr
          | '(' expression ')'                        # parenExpr
          | NUMBER                                    # numberExpr
          | IDENTIFIER                                # idExpr
          | STRING                                    # stringExpr
          ;

// токены
IDENTIFIER       : [a-zA-Z_] [a-zA-Z_0-9]* ;  // идентификаторы (переменные)
NUMBER           : [0-9]+ ;                   // целые числа
STRING           : '"' ('.' | ~'"')* '"';     // строка, может содержать экранированные символы


// операторы
PLUS             : '+' ;
MINUS            : '-' ;
MUL              : '*' ;
DIV              : '/' ;
AND              : '&&' ;
OR               : '||' ;
NOT              : '!' ;

// операторы сравнения
GT               : '>' ;
LT               : '<' ;
GE               : '>=' ;
LE               : '<=' ;
EQ               : '==' ;
NEQ              : '!=' ;

// пропуск пробелов и переводов строк
SPACE            : [ \r\n\t]+ -> skip;

COMMENT_NESTED: '/*' .*? '*/' -> skip;
COMMENT_INLINE: '//' ~[\n\r]* -> skip ;