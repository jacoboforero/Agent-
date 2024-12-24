grammar AgentPP;

// --------------
// PARSER RULES
// --------------

program
    : taskDefinition* EOF
    ;

taskDefinition
    : TASK identifier COLON block
    ;

block
    : statement*
    ;

statement
    : command
    | conditional
    | loopStmt
    | assignment
    | execution
    | logStmt
    ;

command
    : READ filepath
    | WRITE expression TO filepath
    | DELETE filepath
    | MOVE filepath TO destination
    | COMPRESS files GT archive
    | EXTRACT archive
    | FETCH url
    | UPLOAD filepath TO destination
    | DOWNLOAD filepath FROM url
    ;

conditional
    : IF condition COLON block ( ELSE COLON block )?
    ;

loopStmt
    : LOOP block UNTIL condition
    ;

assignment
    : identifier EQUAL expression
    ;

execution
    : EXECUTE taskCall
    | PARALLEL COLON block
    | WAIT taskCall
    | SCHEDULE taskCall AT timeRule
    ;

taskCall
    : identifier ( LPAREN arguments? RPAREN )?
    ;

logStmt
    : LOG stringLiteral
    ;

condition
    : expression comparisonOperator expression
    ;

expression
    : literal
    | identifier
    | functionCall
    | arithmeticExpression
    ;

functionCall
    : identifier LPAREN arguments? RPAREN
    ;

arithmeticExpression
    : expression arithmeticOperator expression
    ;

arguments
    : expression ( COMMA expression )*
    ;

// --------------
// HELPER RULES
// --------------

filepath
    : stringLiteral
    ;

destination
    : stringLiteral
    ;

files
    : stringLiteral ( COMMA stringLiteral )*
    ;

archive
    : stringLiteral
    ;

url
    : stringLiteral
    ;

timeRule
    : stringLiteral
    ;

// --------------
// TERMINALS & TOKENS
// --------------

comparisonOperator
    : EQ
    | NE
    | GEQ
    | LEQ
    | GT_
    | LT_
    ;

arithmeticOperator
    : PLUS
    | MINUS
    | STAR
    | DIV
    ;

// --------------
// LEXER RULES
// --------------

TASK        : 'task';
IF          : 'if';
ELSE        : 'else';
LOOP        : 'loop';
UNTIL       : 'until';
EXECUTE     : 'execute';
PARALLEL    : 'parallel';
SCHEDULE    : 'schedule';
WAIT        : 'wait';
READ        : 'read';
WRITE       : 'write';
TO          : 'to';
FROM        : 'from';
DELETE      : 'delete';
MOVE        : 'move';
COMPRESS    : 'compress';
EXTRACT     : 'extract';
FETCH       : 'fetch';
UPLOAD      : 'upload';
DOWNLOAD    : 'download';
LOG         : 'log';
AT          : 'at';

COLON       : ':';
GT          : '>';
EQUAL       : '=';
PLUS        : '+';
MINUS       : '-';
STAR        : '*';
DIV         : '/';
COMMA       : ',';
LPAREN      : '(';
RPAREN      : ')';

// Comparison operators
EQ          : '==';
NE          : '!=';
GEQ         : '>=';
LEQ         : '<=';
GT_         : '>';
LT_         : '<';

// Literals
fragment DIGIT       : [0-9];
fragment LETTER      : [a-zA-Z];

identifier
    : LETTER (LETTER | DIGIT | '_')*
    ;

// Simple string literal (no advanced escaping shown)
stringLiteral
    : '"' (~["\r\n])* '"'
    ;

// Number
numberLiteral
    : MINUS? DIGIT+
    ;

// Boolean
booleanLiteral
    : 'true'
    | 'false'
    ;

// Whitespace and newlines
WS
    : [ \t\r\n]+ -> skip
    ;

// --------------
// Fragments
// --------------

literal
    : stringLiteral
    | numberLiteral
    | booleanLiteral
    ;

