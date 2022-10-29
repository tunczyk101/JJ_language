lexer grammar jj_value_types_lexer
	;

NUMBER_TYPE
	: NUMBER_SIGN? (INT | FLOAT)
	;

NUMBER_SIGN
	: '-'
	| '+'
	;

DIGIT
	: [0-9]
	;

INT
	: DIGIT+
	;

FLOAT
	: INT '.' INT
	;

BOOL
	: 'true'
	| 'false'
	;
