parser grammar jjParser
	;

options
{
	tokenVocab= jjLexer;
}

prog
	: global_line* function_main
	;

global_line
	: COMMENT
	| function
	;

function
	: FUNC_DECL COMMENT? NAME COMMENT? optinal_function_blocks
	;

function_main
	: FUNC_DECL COMMENT? MAIN_FUNC_NAME COMMENT? structural_block? COMMENT?
	;

optinal_function_blocks
	: arguments_block? COMMENT? where_block? COMMENT? structural_block? COMMENT? return_block?
	;

arguments_block
	: WITH_DECL
	;

structural_block
	: BLOCK_BEGIN structural_line* BLOCK_END
	;

return_block
	: RETURN_DECL COMMENT? (NAME | value)
	;

where_block
	: WHERE_DECL COMMENT? expresion
	;

structural_line
	: structural_line_instruction+ COMMENT?
	| COMMENT
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
	: value
	| NAME
	;

value
	: NUMBER_TYPE
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