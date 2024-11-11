grammar OurLang;

// начальное правило грамматики
program: (statement)* EOF;

statement: printStatement ;

printStatement: 'print' ' ' NUMBER ';' ;

// токены
NUMBER          : [0-9]+ ;       // целые числа
SPACE           : [ \r\n\t]+ -> skip;  // пропуск пробелов и переносов строк