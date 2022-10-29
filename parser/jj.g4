parser grammar jj
	;

options
{
	tokenVocab= jj_lexer;
}

prog
	: function* function_main
	;

function
	: FUNC_DECL NAME optinal_function_blocks
	;

function_main
	: FUNC_DECL MAIN_FUNC_NAME optinal_function_blocks
	;

optinal_function_blocks
	: arguments_block? where_block? structural_block? return_block?
	;

arguments_block
	: WITH_DECL
	;

structural_block
	: BLOCK_BEGIN structural_line_instruction* BLOCK_END
	;

return_block
	: RETURN_DECL (NAME | value)
	;

where_block
	: WHERE_DECL expresion
	;

structural_line
	: structural_line_instruction* COMMENT?
	| COMMENT
	| // empty
	;

variable_declaration
	: VARIABLE_TOKEN MUTABLE_TOKEN? NAME BLOCK_BEGIN expresion BLOCK_END
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
	: NAME
	| value
	;

value
	: NUMBER
	| BOOL
	;
