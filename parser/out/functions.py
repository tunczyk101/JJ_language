from typing import Any, Optional, Callable
from dataclasses import dataclass

if __name__ is not None and "." in __name__:
    from .jjParser import jjParser
else:
    from jjParser import jjParser

class VariadicArguments:
    pass

@dataclass
class Function_Argument:
    name: str
    is_mutable: bool

    @staticmethod
    def from_argument_decl(argument_decl: jjParser.Argument_declContext) -> 'Function_Argument':
        return Function_Argument(str(argument_decl.NAME()), argument_decl.MUTABLE_TOKEN() is not None)

    @staticmethod
    def parse_all(argument_block: jjParser.Arguments_blockContext) -> list['Function_Argument']:
        arguments = []
        
        if(argument_block is None):
            return arguments
        
        arguments.append(Function_Argument.from_argument_decl(argument_block.argument_decl()))
        for additional_argument in argument_block.additional_arguments_decl():
            arguments.append(Function_Argument.from_argument_decl(additional_argument.argument_decl()))
        return arguments

@dataclass
class Function_specialization:
    guard_block: Optional[jjParser.ExpresionContext]
    body_block: Optional[jjParser.Structural_blockContext]
    return_block: Optional[jjParser.Return_blockContext]

    @staticmethod
    def from_optional_function_blocks(optional_function_blocks: jjParser.Optinal_function_blocksContext) -> 'Function_specialization':
        return Function_specialization(optional_function_blocks.guard_block(), optional_function_blocks.structural_block(), optional_function_blocks.return_block())

@dataclass
class Function:
    name: str
    arguments: list[Function_Argument]
    specializations: list[Function_specialization]

    @staticmethod
    def from_function_context(function_context: jjParser.FunctionContext) -> 'Function':
        name = str(function_context.NAME())
        arguments = Function_Argument.parse_all(function_context.optinal_function_blocks().arguments_block())
        specialisation = Function_specialization.from_optional_function_blocks(function_context.optinal_function_blocks())
        
        return Function(name, arguments, [specialisation])

def str_variable(arg):
    if(isinstance(arg, bool)):
        return "true" if arg else "false"
    else:
        return str(arg)

def print_with_end(args, end):
    print(' '.join(map(lambda x: str_variable(x), args)), end=end)

def assert_fn(arg, ctx: jjParser.Function_callContext):
    if(not arg):
        assertion_text = ctx.getText()[len("assert("):-1]
        print(f"ERROR: Assertion {assertion_text} failed at {ctx.getSourceInterval}.")
        exit(0)

class STD_function:
    def __init__(self, arguments_count: int|VariadicArguments, body: Callable[[list[Any]], Any]):
        self.arguments_count = arguments_count
        self.body = body

    def call(self, args: list[Any], ctx: jjParser.Function_callContext):
        return self.body(args, ctx)

STANDARD_FUNCTIONS = {
    'println':  STD_function(VariadicArguments(), lambda args, _: print_with_end(args, end='\n')),
    'print':    STD_function(VariadicArguments(), lambda args, _: print_with_end(args, end='')),
    'assert':   STD_function(1, lambda args, ctx: assert_fn(args[0], ctx))
}
    
