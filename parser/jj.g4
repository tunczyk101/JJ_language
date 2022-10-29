grammar jj
	;

prog
	: function* function_main
	;

function
	: FUNC_DECL name optinal_function_blocks
	;

function_main
	: FUNC_DECL MAIN_FUNC_NAME optinal_function_blocks
	;

optinal_function_blocks
	: arguments_block? structural_block? return_block?
	;

arguments_block
	: WITH_DECL
	;

structural_block
	: BLOCK_BEGIN structural_line_instruction* BLOCK_END
	;

return_block
	: RETURN_DECL (name | value)
	;

structural_line
	: structural_line_instruction* COMMENT?
	| COMMENT
	|			// empty
	;

variable_declaration
	: VARIABLE_TOKEN MUTABLE_TOKEN? name BLOCK_BEGIN expresion BLOCK_END
	;

structural_line_instruction
	: instruction? END_OF_INSTRUCTION
	;

instruction
	: variable_declaration
	| expresion
	;

expresion
	: identifier
	| NESTED_EXPR_BEGIN expresion NESTED_EXPR_END
	| (identifier | NESTED_EXPR_BEGIN expresion NESTED_EXPR_END) BIN_OPERATION_TOKEN expresion
	;

identifier
	: name
	| value
	;

value
	: NUMBER
	| BOOL
	;

name
	: NAME_start NAME_continue*
	;
// NAMES  ---------------------------------------------------------------------- 
NAME_start
	: '_'
	| [A-Z]
	| [a-z]
	;

NAME_continue
	: NAME_start
	| [0-9]
	;
// VALUE TYPES  ---------------------------------------------------------------------- 
NUMBER
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
// -----------------------------------------------------------------------------
FUNC_DECL
	: 'func'
	;

MAIN_FUNC_NAME
	: 'main'
	|
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
// -----------------------------------------------------------------------------
COMMENT
	: '//' ~[\r\n\f]*
	;

WS
	: [ \t]+	-> skip
	;

NEW_LINE
	: ('\r'? '\n' | '\r' | '\f') WS?
	;