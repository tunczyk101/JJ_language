lexer grammar jj_types_lexer
	;

TYPE_NAME
	: INT_TYPE
	| FLOAT_TYPE
	| BOOL_TYPE
	;

INT_TYPE
	: 'int'
	;

FLOAT_TYPE
	: 'float'
	;

BOOL_TYPE
	: 'bool'
	;