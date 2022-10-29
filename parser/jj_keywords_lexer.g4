lexer grammar jj_keywords_lexer
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

PARENTHESES_BEGIN
	: '('
	;

PARENTHESES_END
	: ')'
	;

UNARY_OR_BINARY_OPERATIONS
	: '+'
	| '-'
	;

ONLY_UNARY_OPERATIONS
	: '!'
	;

ONLY_BINARY_OPERATIONS
	: '*'
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

ASSIGNMENT_TOKEN
	: '='
	;

RETURN_DECL
	: 'returns'
	;

WITH_DECL
	: 'with'
	;

WHERE_DECL
	: 'where'
	;

IF_DECL
	: 'if'
	;

ELSE_DECL
	: 'else'
	;

WHILE_DECL
	: 'while'
	;

FOR_DECL
	: 'for'
	;
