lexer grammar jj_value_types_lexer
	;

NUMBER_TYPE
	: INT ('.' INT)?
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
