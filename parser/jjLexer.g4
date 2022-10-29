lexer grammar jjLexer
	;

import jj_value_types_lexer, jj_keywords_lexer, jj_names_lexer
	;

COMMENT_START
	: '//'
	;
// -----------------------------------------------------------------------------
COMMENT
	: COMMENT_START ~[\r\n\f]* NEW_LINE
	;

WS
	: [ \t\r\n]+ -> skip
	;

NEW_LINE
	: ('\r'? '\n' | '\r' | '\f') WS?
	;
// -----------------------------------------------------------------------------
