grammar OurLang;

// начальное правило грамматики
program: (statement)* EOF;

// список возможных операторов
statement: varDeclaration
    | varAssignment          // присваивание значения
    | funcDefinition         // определение функции
    | funcCall               // вызов функции
    | outputStatement        // вывод на экран
    | returnStatement        // возврат из функции
    | ifStatement            // условный оператор
    | whileLoop              // цикл while
    | forLoop                // цикл for
    | codeBlock              // блок кода
    ;

// список возможных выражений
expression: '(' expression ')'                                  # parenthesisExpr
    | left=expression op=(ASTERISK | SLASH) right=expression    # mulDivExpr
    | left=expression op=(PLUS | MINUS) right=expression        # plusMinusExpr
    | left=expression compOperator right=expression             # compExpr
    | IDENTIFIER                                                # idExpr
    | NUMBER                                                    # numExpr
    | DOUBLE_NUMBER                                             # doubleExpr
    | STRING_LITERAL                                            # stringExpr
    | funcCall                                                  # funcCallExpr
    ;

// описание переменной
varDeclaration: 'var' IDENTIFIER ('=' expression)? ;

// присваивание
varAssignment: IDENTIFIER '=' expression ;

// оператор сравнения
compOperator: op=(LESS | LESS_OR_EQUAL | EQUAL | NOT_EQUAL | GREATER | GREATER_OR_EQUAL) ;

// вывод на экран
outputStatement: 'println' expression ;

// возврат из функции
returnStatement: 'return' expression? ;

// блок кода
codeBlock: '{' (statement)* '}' ;

// вызов функции
funcCall: IDENTIFIER '(' (expression (',' expression)*)? ')' ;

// определение функции
funcDefinition: 'fun' IDENTIFIER '(' (IDENTIFIER (',' IDENTIFIER)*)? ')' '{' (statement)* '}' ;

// условный оператор с поддержкой elif и else
ifStatement
    : 'if' '(' expression ')' statement (elifClause)* (elseClause)?
    ;

elifClause: 'elif' '(' expression ')' statement ;

elseClause: 'else' statement ;

// цикл while
whileLoop: 'while' '(' expression ')' statement ;

// цикл for
forLoop
    : 'for' '(' varDeclaration ';' expression ';' varAssignment ')' statement
    ;

// список токенов
IDENTIFIER          : [a-zA-Z_] [a-zA-Z_0-9]* ;
NUMBER              : [0-9]+ ;
DOUBLE_NUMBER       : NUMBER '.' NUMBER ;
STRING_LITERAL      : '"' (~["])* '"' ;

ASTERISK            : '*' ;
SLASH               : '/' ;
PLUS                : '+' ;
MINUS               : '-' ;

ASSIGN              : '=' ;
EQUAL               : '==' ;
NOT_EQUAL           : '!=' ;
LESS                : '<' ;
LESS_OR_EQUAL       : '<=' ;
GREATER             : '>' ;
GREATER_OR_EQUAL    : '>=' ;

// пропуск пробелов и комментариев
SPACE               : [ \r\n\t]+ -> skip ;
LINE_COMMENT        : '//' ~[\n\r]* -> skip ;
BLOCK_COMMENT       : '/*' .*? '*/' -> skip ;
