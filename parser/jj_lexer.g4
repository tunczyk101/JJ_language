lexer grammar jj_lexer
	;

import jj_names_lexer, jj_value_types_lexer
	;

FUNC_DECL
	: 'func'
	;

MAIN_FUNC_NAME
	: 'main'
	;

VARIABLE_TOKEN
	: 'let'
	;

MUTABLE_TOKEN
	: 'mut'
	;

END_OF_INSTRUCTION
	: ';'
	;

BLOCK_BEGIN
	: '{'
	;

BLOCK_END
	: '}'
	;

NESTED_EXPR_BEGIN
	: '('
	;

NESTED_EXPR_END
	: ')'
	;

BIN_OPERATION_TOKEN
	: '+'
	| '-'
	| '*'
	| '/'
	| '%'
	| '=='
	| '!='
	| '<'
	| '>'
	| '<='
	| '>='
	| '||'
	| '&&'
	;

RETURN_DECL
	: 'returns'
	;

WITH_DECL
	: 'with'
	;

COMMENT_START
	: '//'
	;
// -----------------------------------------------------------------------------
COMMENT
	: COMMENT_START ~[\r\n\f]*
	;

WS
	: [ \t]+ -> skip
	;

NEW_LINE
	: ('\r'? '\n' | '\r' | '\f') WS?
	;
// -----------------------------------------------------------------------------
