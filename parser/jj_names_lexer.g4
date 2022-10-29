lexer grammar jj_names_lexer
	;

NAME
	: NAME_start NAME_continue*
	;

fragment NAME_start
	: '_'
	| [A-Z]
	| [a-z]
	;

fragment NAME_continue
	: NAME_start
	| [0-9]
	;