grammar AgentPP_ANTLR4Grammar;

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
    | LIST directory
    | ALERT message
    | ANALYZE data WITH model
    | SUMMARIZE data
    | PREDICT input USING model
    | TRAIN model WITH data
    | FILTER data WHERE condition
    | TRANSFORM data WITH function
    | SORT data BY key
    | AGGREGATE data USING function
    | NOTIFY recipient
    | LOG message
    | CURRENT_TIME
    | QUERY_API url
    | EMAIL sender recipient
    ;

conditional
    : IF condition COLON block (ELSE COLON block)?
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
    | SCHEDULE taskCall AT timerule
    ;

logStmt
    : LOG stringLiteral
    ;

expression
    : primaryExpression (arithmeticOperator primaryExpression)*
    ;

primaryExpression
    : literal
    | identifier
    | functionCall
    ;

functionCall
    : identifier LPAREN arguments? RPAREN
    ;

condition
    : expression comparisonOperator expression
    ;

arguments
    : expression (COMMA expression)*
    ;

literal
    : stringLiteral
    | numberLiteral
    | booleanLiteral
    ;

// --------------
// LEXER RULES
// --------------

TASK       : 'task';
IF         : 'if';
ELSE       : 'else';
LOOP       : 'loop';
UNTIL      : 'until';
EXECUTE    : 'execute';
PARALLEL   : 'parallel';
SCHEDULE   : 'schedule';
WAIT       : 'wait';
READ       : 'read';
WRITE      : 'write';
TO         : 'to';
FROM       : 'from';
DELETE     : 'delete';
MOVE       : 'move';
COMPRESS   : 'compress';
EXTRACT    : 'extract';
FETCH      : 'fetch';
UPLOAD     : 'upload';
DOWNLOAD   : 'download';
LOG        : 'log';
ALERT      : 'alert';
ANALYZE    : 'analyze';
SUMMARIZE  : 'summarize';
PREDICT    : 'predict';
TRAIN      : 'train';
FILTER     : 'filter';
TRANSFORM  : 'transform';
SORT       : 'sort';
AGGREGATE  : 'aggregate';
NOTIFY     : 'notify';
CURRENT_TIME : 'current_time';
QUERY_API  : 'query_api';
EMAIL      : 'email';
LIST       : 'list';
WITH       : 'with';
USING      : 'using';
WHERE      : 'where';
BY         : 'by';
AT         : 'at';
COLON      : ':';
GT         : '>';
EQUAL      : '=';
PLUS       : '+';
MINUS      : '-';
STAR       : '*';
DIV        : '/';
COMMA      : ',';
LPAREN     : '(';
RPAREN     : ')';

comparisonOperator
    : '=='
    | '!='
    | '>'
    | '>='
    | '<'
    | '<='
    ;

arithmeticOperator
    : PLUS
    | MINUS
    | STAR
    | DIV
    ;

// --------------
// FRAGMENTS
// --------------
fragment DIGIT : [0-9];
fragment LETTER : [a-zA-Z];

identifier
    : LETTER (LETTER | DIGIT | '_')*
    ;

stringLiteral
    : '"' (~('"' | '\r' | '\n'))* '"'
    ;

numberLiteral
    : MINUS? DIGIT+
    ;

booleanLiteral
    : 'true'
    | 'false'
    ;

filepath
    : stringLiteral
    ;

destination
    : stringLiteral
    ;

directory
    : stringLiteral
    ;

files
    : stringLiteral (COMMA stringLiteral)*
    ;

archive
    : stringLiteral
    ;

url
    : stringLiteral
    ;

data
    : stringLiteral
    ;

model
    : stringLiteral
    ;

recipient
    : stringLiteral
    ;

message
    : stringLiteral
    ;

sender
    : stringLiteral
    ;

key
    : stringLiteral
    ;

function
    : stringLiteral
    ;

taskCall
    : identifier (LPAREN arguments? RPAREN)?
    ;

timerule
    : stringLiteral
    ;

input
    : stringLiteral
    ;
