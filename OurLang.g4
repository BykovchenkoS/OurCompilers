grammar OurLang;
hello : 'hello' ID ;
ID : [a-z]+ ;
WS : [ \t\r\n]+ -> skip ;