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
	: arguments_block? COMMENT? guard_block? COMMENT? structural_block? COMMENT? return_block?
	;

argument_decl
	: MUTABLE_TOKEN? NAME
	;

additional_arguments_decl
	: COMMENT? COMMA_TOKEN COMMENT? argument_decl
	;

arguments_block
	: WITH_DECL COMMENT? argument_decl additional_arguments_decl* COMMENT?
	;

structural_block
	: BLOCK_BEGIN structural_line* BLOCK_END
	;

return_block
	: RETURN_DECL COMMENT? expresion
	;

guard_block
	: WHEN_DECL COMMENT? expresion
	;

structural_line
	: structural_line_instruction+ COMMENT?
	| COMMENT
	;

variable_declaration
	: VARIABLE_TOKEN MUTABLE_TOKEN? NAME BLOCK_BEGIN expresion BLOCK_END
	;

instruction_line
	: instruction? END_OF_INSTRUCTION
	;

structural_line_instruction
	: instruction_line
	| statement
	| structural_block
	;

statement
	: while_statement
	| if_statement
	| for_statement
	;

instruction
	: variable_declaration
	| assignmnet_statement
	| expresion
	;

expresion_in_parenthesis
	: PARENTHESES_BEGIN expresion PARENTHESES_END
	;

left_of_binary_operation
	: identifier
	| expresion_in_parenthesis
	| function_call
	;

all_binary_operations
	: ONLY_BINARY_OPERATIONS
	| UNARY_OR_BINARY_OPERATIONS
	;

all_unary_operations
	: ONLY_UNARY_OPERATIONS
	| UNARY_OR_BINARY_OPERATIONS
	;

expresion
	: identifier
	| expresion_in_parenthesis
	| function_call
	| all_unary_operations expresion
	| left_of_binary_operation all_binary_operations expresion
	;

function_call
	: NAME PARENTHESES_BEGIN expresion PARENTHESES_END
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
	: FOR_DECL PARENTHESES_BEGIN instruction_line instruction_line instruction PARENTHESES_END
		structural_block
	;

assignmnet_statement
	: NAME ASSIGNMENT_TOKEN expresion
	;