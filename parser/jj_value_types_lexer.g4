lexer grammar jj_value_types_lexer
	;

NUMBER_TYPE
	: NUMBER_SIGN? INT ('.' INT)?
	;

fragment NUMBER_SIGN
	: '-'
	| '+'
	;

fragment DIGIT
	: '0' ..'9'
	;

fragment INT
	: DIGIT+
	;

BOOL
	: 'true'
	| 'false'
	;
