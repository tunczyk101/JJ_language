parser grammar jjParser
	;

options
{
	tokenVocab= jjLexer;
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

expresion_in_parenthesis
	: PARENTHESES_BEGIN expresion PARENTHESES_END
	;

expresion
	: identifier
	| expresion_in_parenthesis
	| (identifier | expresion_in_parenthesis) BIN_OPERATION_TOKEN expresion
	;

identifier
	: NAME
	| value
	;

value
	: NUMBER
	| BOOL
	;

if_statement_start
	: IF_DECL expresion_in_parenthesis
	;

if_statement
	: if_statement_start structural_block else_statement?
	;

else_statement
	: ELSE_DECL if_statement_start? structural_block
	;

while_statement
	: WHILE_DECL expresion_in_parenthesis structural_block
	;

for_statement
	: FOR_DECL PARENTHESES_BEGIN structural_line_instruction structural_line_instruction
		structural_line_instruction PARENTHESES_END structural_block
	;