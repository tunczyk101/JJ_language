lexer grammar jj_names_lexer
	;

NAME
	: NAME_start NAME_continue*
	;
NAME_start
	: '_'
	| [A-Z]
	| [a-z]
	;

NAME_continue
	: NAME_start
	| [0-9]
	;