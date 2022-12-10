# Generated from jjParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,1,1,1,3,1,77,8,1,1,2,1,2,3,
        2,81,8,2,1,2,1,2,3,2,85,8,2,1,2,1,2,1,3,1,3,3,3,91,8,3,1,3,1,3,3,
        3,95,8,3,1,3,3,3,98,8,3,1,3,3,3,101,8,3,1,4,3,4,104,8,4,1,4,3,4,
        107,8,4,1,4,3,4,110,8,4,1,4,3,4,113,8,4,1,4,3,4,116,8,4,1,4,3,4,
        119,8,4,1,4,3,4,122,8,4,1,5,3,5,125,8,5,1,5,1,5,1,6,3,6,130,8,6,
        1,6,1,6,3,6,134,8,6,1,6,1,6,1,7,1,7,3,7,140,8,7,1,7,1,7,5,7,144,
        8,7,10,7,12,7,147,9,7,1,7,3,7,150,8,7,1,8,1,8,5,8,154,8,8,10,8,12,
        8,157,9,8,1,8,1,8,1,9,1,9,3,9,163,8,9,1,9,1,9,1,10,1,10,3,10,169,
        8,10,1,10,1,10,1,11,4,11,174,8,11,11,11,12,11,175,1,11,3,11,179,
        8,11,1,11,3,11,182,8,11,1,12,1,12,3,12,186,8,12,1,12,1,12,1,12,1,
        12,1,12,1,13,3,13,194,8,13,1,13,1,13,1,14,1,14,1,14,3,14,201,8,14,
        1,15,1,15,1,15,3,15,206,8,15,1,16,1,16,1,16,3,16,211,8,16,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,3,18,220,8,18,1,19,1,19,1,19,1,19,1,
        20,1,20,1,20,1,20,3,20,230,8,20,1,21,1,21,1,22,1,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,247,8,23,1,24,1,
        24,1,24,1,24,1,24,5,24,254,8,24,10,24,12,24,257,9,24,1,24,1,24,1,
        25,1,25,3,25,263,8,25,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,3,
        28,273,8,28,1,29,1,29,1,29,3,29,278,8,29,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,0,0,
        33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,0,3,2,0,17,17,19,19,1,0,17,18,1,
        0,5,6,311,0,69,1,0,0,0,2,76,1,0,0,0,4,78,1,0,0,0,6,88,1,0,0,0,8,
        103,1,0,0,0,10,124,1,0,0,0,12,129,1,0,0,0,14,137,1,0,0,0,16,151,
        1,0,0,0,18,160,1,0,0,0,20,166,1,0,0,0,22,181,1,0,0,0,24,183,1,0,
        0,0,26,193,1,0,0,0,28,200,1,0,0,0,30,205,1,0,0,0,32,210,1,0,0,0,
        34,212,1,0,0,0,36,219,1,0,0,0,38,221,1,0,0,0,40,229,1,0,0,0,42,231,
        1,0,0,0,44,233,1,0,0,0,46,246,1,0,0,0,48,248,1,0,0,0,50,262,1,0,
        0,0,52,264,1,0,0,0,54,266,1,0,0,0,56,269,1,0,0,0,58,274,1,0,0,0,
        60,279,1,0,0,0,62,283,1,0,0,0,64,291,1,0,0,0,66,68,3,2,1,0,67,66,
        1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,
        71,69,1,0,0,0,72,73,3,6,3,0,73,1,1,0,0,0,74,77,5,2,0,0,75,77,3,4,
        2,0,76,74,1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,80,5,7,0,0,79,81,
        5,2,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,84,5,33,0,0,
        83,85,5,2,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,3,
        8,4,0,87,5,1,0,0,0,88,90,5,7,0,0,89,91,5,2,0,0,90,89,1,0,0,0,90,
        91,1,0,0,0,91,92,1,0,0,0,92,94,5,8,0,0,93,95,5,2,0,0,94,93,1,0,0,
        0,94,95,1,0,0,0,95,97,1,0,0,0,96,98,3,16,8,0,97,96,1,0,0,0,97,98,
        1,0,0,0,98,100,1,0,0,0,99,101,5,2,0,0,100,99,1,0,0,0,100,101,1,0,
        0,0,101,7,1,0,0,0,102,104,3,14,7,0,103,102,1,0,0,0,103,104,1,0,0,
        0,104,106,1,0,0,0,105,107,5,2,0,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,109,1,0,0,0,108,110,3,20,10,0,109,108,1,0,0,0,109,110,1,0,
        0,0,110,112,1,0,0,0,111,113,5,2,0,0,112,111,1,0,0,0,112,113,1,0,
        0,0,113,115,1,0,0,0,114,116,3,16,8,0,115,114,1,0,0,0,115,116,1,0,
        0,0,116,118,1,0,0,0,117,119,5,2,0,0,118,117,1,0,0,0,118,119,1,0,
        0,0,119,121,1,0,0,0,120,122,3,18,9,0,121,120,1,0,0,0,121,122,1,0,
        0,0,122,9,1,0,0,0,123,125,5,10,0,0,124,123,1,0,0,0,124,125,1,0,0,
        0,125,126,1,0,0,0,126,127,5,33,0,0,127,11,1,0,0,0,128,130,5,2,0,
        0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,133,5,12,0,
        0,132,134,5,2,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,
        0,135,136,3,10,5,0,136,13,1,0,0,0,137,139,5,22,0,0,138,140,5,2,0,
        0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,145,3,10,5,
        0,142,144,3,12,6,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,
        0,145,146,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,148,150,5,2,0,
        0,149,148,1,0,0,0,149,150,1,0,0,0,150,15,1,0,0,0,151,155,5,13,0,
        0,152,154,3,22,11,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,
        0,0,155,156,1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,5,14,
        0,0,159,17,1,0,0,0,160,162,5,21,0,0,161,163,5,2,0,0,162,161,1,0,
        0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,3,46,23,0,165,19,1,0,
        0,0,166,168,5,23,0,0,167,169,5,2,0,0,168,167,1,0,0,0,168,169,1,0,
        0,0,169,170,1,0,0,0,170,171,3,46,23,0,171,21,1,0,0,0,172,174,3,28,
        14,0,173,172,1,0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,
        0,0,176,178,1,0,0,0,177,179,5,2,0,0,178,177,1,0,0,0,178,179,1,0,
        0,0,179,182,1,0,0,0,180,182,5,2,0,0,181,173,1,0,0,0,181,180,1,0,
        0,0,182,23,1,0,0,0,183,185,5,9,0,0,184,186,5,10,0,0,185,184,1,0,
        0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,5,33,0,0,188,189,5,13,
        0,0,189,190,3,46,23,0,190,191,5,14,0,0,191,25,1,0,0,0,192,194,3,
        32,16,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,196,
        5,11,0,0,196,27,1,0,0,0,197,201,3,26,13,0,198,201,3,30,15,0,199,
        201,3,16,8,0,200,197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,
        29,1,0,0,0,202,206,3,60,30,0,203,206,3,56,28,0,204,206,3,62,31,0,
        205,202,1,0,0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,31,1,0,0,0,207,
        211,3,24,12,0,208,211,3,64,32,0,209,211,3,46,23,0,210,207,1,0,0,
        0,210,208,1,0,0,0,210,209,1,0,0,0,211,33,1,0,0,0,212,213,5,15,0,
        0,213,214,3,46,23,0,214,215,5,16,0,0,215,35,1,0,0,0,216,220,3,50,
        25,0,217,220,3,34,17,0,218,220,3,48,24,0,219,216,1,0,0,0,219,217,
        1,0,0,0,219,218,1,0,0,0,220,37,1,0,0,0,221,222,3,36,18,0,222,223,
        5,28,0,0,223,224,5,29,0,0,224,39,1,0,0,0,225,230,3,38,19,0,226,230,
        3,50,25,0,227,230,3,34,17,0,228,230,3,48,24,0,229,225,1,0,0,0,229,
        226,1,0,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,41,1,0,0,0,231,232,
        7,0,0,0,232,43,1,0,0,0,233,234,7,1,0,0,234,45,1,0,0,0,235,247,3,
        38,19,0,236,247,3,50,25,0,237,247,3,34,17,0,238,247,3,48,24,0,239,
        240,3,44,22,0,240,241,3,46,23,0,241,247,1,0,0,0,242,243,3,40,20,
        0,243,244,3,42,21,0,244,245,3,46,23,0,245,247,1,0,0,0,246,235,1,
        0,0,0,246,236,1,0,0,0,246,237,1,0,0,0,246,238,1,0,0,0,246,239,1,
        0,0,0,246,242,1,0,0,0,247,47,1,0,0,0,248,249,5,33,0,0,249,250,5,
        15,0,0,250,255,3,46,23,0,251,252,5,12,0,0,252,254,3,46,23,0,253,
        251,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,
        258,1,0,0,0,257,255,1,0,0,0,258,259,5,16,0,0,259,49,1,0,0,0,260,
        263,3,52,26,0,261,263,5,33,0,0,262,260,1,0,0,0,262,261,1,0,0,0,263,
        51,1,0,0,0,264,265,7,2,0,0,265,53,1,0,0,0,266,267,5,24,0,0,267,268,
        3,34,17,0,268,55,1,0,0,0,269,270,3,54,27,0,270,272,3,16,8,0,271,
        273,3,58,29,0,272,271,1,0,0,0,272,273,1,0,0,0,273,57,1,0,0,0,274,
        277,5,25,0,0,275,278,3,56,28,0,276,278,3,16,8,0,277,275,1,0,0,0,
        277,276,1,0,0,0,278,59,1,0,0,0,279,280,5,26,0,0,280,281,3,34,17,
        0,281,282,3,16,8,0,282,61,1,0,0,0,283,284,5,27,0,0,284,285,5,15,
        0,0,285,286,3,26,13,0,286,287,3,26,13,0,287,288,3,32,16,0,288,289,
        5,16,0,0,289,290,3,16,8,0,290,63,1,0,0,0,291,292,5,33,0,0,292,293,
        5,20,0,0,293,294,3,46,23,0,294,65,1,0,0,0,39,69,76,80,84,90,94,97,
        100,103,106,109,112,115,118,121,124,129,133,139,145,149,155,162,
        168,175,178,181,185,193,200,205,210,219,229,246,255,262,272,277
    ]

class jjParser ( Parser ):

    grammarFileName = "jjParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'//'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'func'", "'main'", "'let'", 
                     "'mut'", "';'", "','", "'{'", "'}'", "'('", "')'", 
                     "<INVALID>", "'!'", "<INVALID>", "'='", "'returns'", 
                     "'with'", "'when'", "'if'", "'else'", "'while'", "'for'", 
                     "'as'", "<INVALID>", "'int'", "'float'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_START", "COMMENT", "WS", "NEW_LINE", 
                      "NUMBER_TYPE", "BOOL", "FUNC_DECL", "MAIN_FUNC_NAME", 
                      "VARIABLE_TOKEN", "MUTABLE_TOKEN", "END_OF_INSTRUCTION", 
                      "COMMA_TOKEN", "BLOCK_BEGIN", "BLOCK_END", "PARENTHESES_BEGIN", 
                      "PARENTHESES_END", "UNARY_OR_BINARY_OPERATIONS", "ONLY_UNARY_OPERATIONS", 
                      "ONLY_BINARY_OPERATIONS", "ASSIGNMENT_TOKEN", "RETURN_DECL", 
                      "WITH_DECL", "WHEN_DECL", "IF_DECL", "ELSE_DECL", 
                      "WHILE_DECL", "FOR_DECL", "CAST_DECL", "TYPE_NAME", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "NAME" ]

    RULE_prog = 0
    RULE_global_line = 1
    RULE_function = 2
    RULE_function_main = 3
    RULE_optinal_function_blocks = 4
    RULE_argument_decl = 5
    RULE_additional_arguments_decl = 6
    RULE_arguments_block = 7
    RULE_structural_block = 8
    RULE_return_block = 9
    RULE_guard_block = 10
    RULE_structural_line = 11
    RULE_variable_declaration = 12
    RULE_instruction_line = 13
    RULE_structural_line_instruction = 14
    RULE_statement = 15
    RULE_instruction = 16
    RULE_expresion_in_parenthesis = 17
    RULE_left_of_cast_expr = 18
    RULE_cast_expression = 19
    RULE_left_of_binary_operation = 20
    RULE_all_binary_operations = 21
    RULE_all_unary_operations = 22
    RULE_expresion = 23
    RULE_function_call = 24
    RULE_identifier = 25
    RULE_value = 26
    RULE_if_statement_start = 27
    RULE_if_statement = 28
    RULE_else_statement = 29
    RULE_while_statement = 30
    RULE_for_statement = 31
    RULE_assignmnet_statement = 32

    ruleNames =  [ "prog", "global_line", "function", "function_main", "optinal_function_blocks", 
                   "argument_decl", "additional_arguments_decl", "arguments_block", 
                   "structural_block", "return_block", "guard_block", "structural_line", 
                   "variable_declaration", "instruction_line", "structural_line_instruction", 
                   "statement", "instruction", "expresion_in_parenthesis", 
                   "left_of_cast_expr", "cast_expression", "left_of_binary_operation", 
                   "all_binary_operations", "all_unary_operations", "expresion", 
                   "function_call", "identifier", "value", "if_statement_start", 
                   "if_statement", "else_statement", "while_statement", 
                   "for_statement", "assignmnet_statement" ]

    EOF = Token.EOF
    COMMENT_START=1
    COMMENT=2
    WS=3
    NEW_LINE=4
    NUMBER_TYPE=5
    BOOL=6
    FUNC_DECL=7
    MAIN_FUNC_NAME=8
    VARIABLE_TOKEN=9
    MUTABLE_TOKEN=10
    END_OF_INSTRUCTION=11
    COMMA_TOKEN=12
    BLOCK_BEGIN=13
    BLOCK_END=14
    PARENTHESES_BEGIN=15
    PARENTHESES_END=16
    UNARY_OR_BINARY_OPERATIONS=17
    ONLY_UNARY_OPERATIONS=18
    ONLY_BINARY_OPERATIONS=19
    ASSIGNMENT_TOKEN=20
    RETURN_DECL=21
    WITH_DECL=22
    WHEN_DECL=23
    IF_DECL=24
    ELSE_DECL=25
    WHILE_DECL=26
    FOR_DECL=27
    CAST_DECL=28
    TYPE_NAME=29
    INT_TYPE=30
    FLOAT_TYPE=31
    BOOL_TYPE=32
    NAME=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_main(self):
            return self.getTypedRuleContext(jjParser.Function_mainContext,0)


        def global_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.Global_lineContext)
            else:
                return self.getTypedRuleContext(jjParser.Global_lineContext,i)


        def getRuleIndex(self):
            return jjParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = jjParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.global_line() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 72
            self.function_main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(jjParser.COMMENT, 0)

        def function(self):
            return self.getTypedRuleContext(jjParser.FunctionContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_global_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_line" ):
                listener.enterGlobal_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_line" ):
                listener.exitGlobal_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_line" ):
                return visitor.visitGlobal_line(self)
            else:
                return visitor.visitChildren(self)




    def global_line(self):

        localctx = jjParser.Global_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_line)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(jjParser.COMMENT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_DECL(self):
            return self.getToken(jjParser.FUNC_DECL, 0)

        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def optinal_function_blocks(self):
            return self.getTypedRuleContext(jjParser.Optinal_function_blocksContext,0)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMENT)
            else:
                return self.getToken(jjParser.COMMENT, i)

        def getRuleIndex(self):
            return jjParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = jjParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(jjParser.FUNC_DECL)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 79
                self.match(jjParser.COMMENT)


            self.state = 82
            self.match(jjParser.NAME)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 83
                self.match(jjParser.COMMENT)


            self.state = 86
            self.optinal_function_blocks()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_DECL(self):
            return self.getToken(jjParser.FUNC_DECL, 0)

        def MAIN_FUNC_NAME(self):
            return self.getToken(jjParser.MAIN_FUNC_NAME, 0)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMENT)
            else:
                return self.getToken(jjParser.COMMENT, i)

        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_function_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_main" ):
                listener.enterFunction_main(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_main" ):
                listener.exitFunction_main(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_main" ):
                return visitor.visitFunction_main(self)
            else:
                return visitor.visitChildren(self)




    def function_main(self):

        localctx = jjParser.Function_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(jjParser.FUNC_DECL)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 89
                self.match(jjParser.COMMENT)


            self.state = 92
            self.match(jjParser.MAIN_FUNC_NAME)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 93
                self.match(jjParser.COMMENT)


            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 96
                self.structural_block()


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 99
                self.match(jjParser.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optinal_function_blocksContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments_block(self):
            return self.getTypedRuleContext(jjParser.Arguments_blockContext,0)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMENT)
            else:
                return self.getToken(jjParser.COMMENT, i)

        def guard_block(self):
            return self.getTypedRuleContext(jjParser.Guard_blockContext,0)


        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def return_block(self):
            return self.getTypedRuleContext(jjParser.Return_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_optinal_function_blocks

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptinal_function_blocks" ):
                listener.enterOptinal_function_blocks(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptinal_function_blocks" ):
                listener.exitOptinal_function_blocks(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptinal_function_blocks" ):
                return visitor.visitOptinal_function_blocks(self)
            else:
                return visitor.visitChildren(self)




    def optinal_function_blocks(self):

        localctx = jjParser.Optinal_function_blocksContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optinal_function_blocks)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 102
                self.arguments_block()


            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 105
                self.match(jjParser.COMMENT)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 108
                self.guard_block()


            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(jjParser.COMMENT)


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 114
                self.structural_block()


            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 117
                self.match(jjParser.COMMENT)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 120
                self.return_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def MUTABLE_TOKEN(self):
            return self.getToken(jjParser.MUTABLE_TOKEN, 0)

        def getRuleIndex(self):
            return jjParser.RULE_argument_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_decl" ):
                listener.enterArgument_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_decl" ):
                listener.exitArgument_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_decl" ):
                return visitor.visitArgument_decl(self)
            else:
                return visitor.visitChildren(self)




    def argument_decl(self):

        localctx = jjParser.Argument_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 123
                self.match(jjParser.MUTABLE_TOKEN)


            self.state = 126
            self.match(jjParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additional_arguments_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA_TOKEN(self):
            return self.getToken(jjParser.COMMA_TOKEN, 0)

        def argument_decl(self):
            return self.getTypedRuleContext(jjParser.Argument_declContext,0)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMENT)
            else:
                return self.getToken(jjParser.COMMENT, i)

        def getRuleIndex(self):
            return jjParser.RULE_additional_arguments_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditional_arguments_decl" ):
                listener.enterAdditional_arguments_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditional_arguments_decl" ):
                listener.exitAdditional_arguments_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditional_arguments_decl" ):
                return visitor.visitAdditional_arguments_decl(self)
            else:
                return visitor.visitChildren(self)




    def additional_arguments_decl(self):

        localctx = jjParser.Additional_arguments_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_additional_arguments_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 128
                self.match(jjParser.COMMENT)


            self.state = 131
            self.match(jjParser.COMMA_TOKEN)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 132
                self.match(jjParser.COMMENT)


            self.state = 135
            self.argument_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arguments_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH_DECL(self):
            return self.getToken(jjParser.WITH_DECL, 0)

        def argument_decl(self):
            return self.getTypedRuleContext(jjParser.Argument_declContext,0)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMENT)
            else:
                return self.getToken(jjParser.COMMENT, i)

        def additional_arguments_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.Additional_arguments_declContext)
            else:
                return self.getTypedRuleContext(jjParser.Additional_arguments_declContext,i)


        def getRuleIndex(self):
            return jjParser.RULE_arguments_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments_block" ):
                listener.enterArguments_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments_block" ):
                listener.exitArguments_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments_block" ):
                return visitor.visitArguments_block(self)
            else:
                return visitor.visitChildren(self)




    def arguments_block(self):

        localctx = jjParser.Arguments_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(jjParser.WITH_DECL)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 138
                self.match(jjParser.COMMENT)


            self.state = 141
            self.argument_decl()
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self.additional_arguments_decl() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(jjParser.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structural_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_BEGIN(self):
            return self.getToken(jjParser.BLOCK_BEGIN, 0)

        def BLOCK_END(self):
            return self.getToken(jjParser.BLOCK_END, 0)

        def structural_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.Structural_lineContext)
            else:
                return self.getTypedRuleContext(jjParser.Structural_lineContext,i)


        def getRuleIndex(self):
            return jjParser.RULE_structural_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructural_block" ):
                listener.enterStructural_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructural_block" ):
                listener.exitStructural_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructural_block" ):
                return visitor.visitStructural_block(self)
            else:
                return visitor.visitChildren(self)




    def structural_block(self):

        localctx = jjParser.Structural_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structural_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(jjParser.BLOCK_BEGIN)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8808475236) != 0:
                self.state = 152
                self.structural_line()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(jjParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_DECL(self):
            return self.getToken(jjParser.RETURN_DECL, 0)

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def COMMENT(self):
            return self.getToken(jjParser.COMMENT, 0)

        def getRuleIndex(self):
            return jjParser.RULE_return_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_block" ):
                listener.enterReturn_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_block" ):
                listener.exitReturn_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_block" ):
                return visitor.visitReturn_block(self)
            else:
                return visitor.visitChildren(self)




    def return_block(self):

        localctx = jjParser.Return_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(jjParser.RETURN_DECL)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 161
                self.match(jjParser.COMMENT)


            self.state = 164
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Guard_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN_DECL(self):
            return self.getToken(jjParser.WHEN_DECL, 0)

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def COMMENT(self):
            return self.getToken(jjParser.COMMENT, 0)

        def getRuleIndex(self):
            return jjParser.RULE_guard_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuard_block" ):
                listener.enterGuard_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuard_block" ):
                listener.exitGuard_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuard_block" ):
                return visitor.visitGuard_block(self)
            else:
                return visitor.visitChildren(self)




    def guard_block(self):

        localctx = jjParser.Guard_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_guard_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(jjParser.WHEN_DECL)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 167
                self.match(jjParser.COMMENT)


            self.state = 170
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structural_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structural_line_instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.Structural_line_instructionContext)
            else:
                return self.getTypedRuleContext(jjParser.Structural_line_instructionContext,i)


        def COMMENT(self):
            return self.getToken(jjParser.COMMENT, 0)

        def getRuleIndex(self):
            return jjParser.RULE_structural_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructural_line" ):
                listener.enterStructural_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructural_line" ):
                listener.exitStructural_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructural_line" ):
                return visitor.visitStructural_line(self)
            else:
                return visitor.visitChildren(self)




    def structural_line(self):

        localctx = jjParser.Structural_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structural_line)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 9, 11, 13, 15, 17, 18, 24, 26, 27, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 172
                        self.structural_line_instruction()

                    else:
                        raise NoViableAltException(self)
                    self.state = 175 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 178
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 177
                    self.match(jjParser.COMMENT)


                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(jjParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_TOKEN(self):
            return self.getToken(jjParser.VARIABLE_TOKEN, 0)

        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def BLOCK_BEGIN(self):
            return self.getToken(jjParser.BLOCK_BEGIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def BLOCK_END(self):
            return self.getToken(jjParser.BLOCK_END, 0)

        def MUTABLE_TOKEN(self):
            return self.getToken(jjParser.MUTABLE_TOKEN, 0)

        def getRuleIndex(self):
            return jjParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = jjParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(jjParser.VARIABLE_TOKEN)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 184
                self.match(jjParser.MUTABLE_TOKEN)


            self.state = 187
            self.match(jjParser.NAME)
            self.state = 188
            self.match(jjParser.BLOCK_BEGIN)
            self.state = 189
            self.expresion()
            self.state = 190
            self.match(jjParser.BLOCK_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_lineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_OF_INSTRUCTION(self):
            return self.getToken(jjParser.END_OF_INSTRUCTION, 0)

        def instruction(self):
            return self.getTypedRuleContext(jjParser.InstructionContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_instruction_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction_line" ):
                listener.enterInstruction_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction_line" ):
                listener.exitInstruction_line(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_line" ):
                return visitor.visitInstruction_line(self)
            else:
                return visitor.visitChildren(self)




    def instruction_line(self):

        localctx = jjParser.Instruction_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_instruction_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 8590361184) != 0:
                self.state = 192
                self.instruction()


            self.state = 195
            self.match(jjParser.END_OF_INSTRUCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structural_line_instructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction_line(self):
            return self.getTypedRuleContext(jjParser.Instruction_lineContext,0)


        def statement(self):
            return self.getTypedRuleContext(jjParser.StatementContext,0)


        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_structural_line_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructural_line_instruction" ):
                listener.enterStructural_line_instruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructural_line_instruction" ):
                listener.exitStructural_line_instruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructural_line_instruction" ):
                return visitor.visitStructural_line_instruction(self)
            else:
                return visitor.visitChildren(self)




    def structural_line_instruction(self):

        localctx = jjParser.Structural_line_instructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structural_line_instruction)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 9, 11, 15, 17, 18, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.instruction_line()
                pass
            elif token in [24, 26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.structural_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_statement(self):
            return self.getTypedRuleContext(jjParser.While_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(jjParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(jjParser.For_statementContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = jjParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.while_statement()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.if_statement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.for_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(jjParser.Variable_declarationContext,0)


        def assignmnet_statement(self):
            return self.getTypedRuleContext(jjParser.Assignmnet_statementContext,0)


        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = jjParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instruction)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.assignmnet_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_in_parenthesisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTHESES_BEGIN(self):
            return self.getToken(jjParser.PARENTHESES_BEGIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def PARENTHESES_END(self):
            return self.getToken(jjParser.PARENTHESES_END, 0)

        def getRuleIndex(self):
            return jjParser.RULE_expresion_in_parenthesis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_in_parenthesis" ):
                listener.enterExpresion_in_parenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_in_parenthesis" ):
                listener.exitExpresion_in_parenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion_in_parenthesis" ):
                return visitor.visitExpresion_in_parenthesis(self)
            else:
                return visitor.visitChildren(self)




    def expresion_in_parenthesis(self):

        localctx = jjParser.Expresion_in_parenthesisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expresion_in_parenthesis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 213
            self.expresion()
            self.state = 214
            self.match(jjParser.PARENTHESES_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_of_cast_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(jjParser.IdentifierContext,0)


        def expresion_in_parenthesis(self):
            return self.getTypedRuleContext(jjParser.Expresion_in_parenthesisContext,0)


        def function_call(self):
            return self.getTypedRuleContext(jjParser.Function_callContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_left_of_cast_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_of_cast_expr" ):
                listener.enterLeft_of_cast_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_of_cast_expr" ):
                listener.exitLeft_of_cast_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_of_cast_expr" ):
                return visitor.visitLeft_of_cast_expr(self)
            else:
                return visitor.visitChildren(self)




    def left_of_cast_expr(self):

        localctx = jjParser.Left_of_cast_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_left_of_cast_expr)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.expresion_in_parenthesis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cast_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_of_cast_expr(self):
            return self.getTypedRuleContext(jjParser.Left_of_cast_exprContext,0)


        def CAST_DECL(self):
            return self.getToken(jjParser.CAST_DECL, 0)

        def TYPE_NAME(self):
            return self.getToken(jjParser.TYPE_NAME, 0)

        def getRuleIndex(self):
            return jjParser.RULE_cast_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast_expression" ):
                listener.enterCast_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast_expression" ):
                listener.exitCast_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast_expression" ):
                return visitor.visitCast_expression(self)
            else:
                return visitor.visitChildren(self)




    def cast_expression(self):

        localctx = jjParser.Cast_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cast_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.left_of_cast_expr()
            self.state = 222
            self.match(jjParser.CAST_DECL)
            self.state = 223
            self.match(jjParser.TYPE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_of_binary_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cast_expression(self):
            return self.getTypedRuleContext(jjParser.Cast_expressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(jjParser.IdentifierContext,0)


        def expresion_in_parenthesis(self):
            return self.getTypedRuleContext(jjParser.Expresion_in_parenthesisContext,0)


        def function_call(self):
            return self.getTypedRuleContext(jjParser.Function_callContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_left_of_binary_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_of_binary_operation" ):
                listener.enterLeft_of_binary_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_of_binary_operation" ):
                listener.exitLeft_of_binary_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_of_binary_operation" ):
                return visitor.visitLeft_of_binary_operation(self)
            else:
                return visitor.visitChildren(self)




    def left_of_binary_operation(self):

        localctx = jjParser.Left_of_binary_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_left_of_binary_operation)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.cast_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.expresion_in_parenthesis()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_binary_operationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONLY_BINARY_OPERATIONS(self):
            return self.getToken(jjParser.ONLY_BINARY_OPERATIONS, 0)

        def UNARY_OR_BINARY_OPERATIONS(self):
            return self.getToken(jjParser.UNARY_OR_BINARY_OPERATIONS, 0)

        def getRuleIndex(self):
            return jjParser.RULE_all_binary_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_binary_operations" ):
                listener.enterAll_binary_operations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_binary_operations" ):
                listener.exitAll_binary_operations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_binary_operations" ):
                return visitor.visitAll_binary_operations(self)
            else:
                return visitor.visitChildren(self)




    def all_binary_operations(self):

        localctx = jjParser.All_binary_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_all_binary_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not(_la==17 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_unary_operationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONLY_UNARY_OPERATIONS(self):
            return self.getToken(jjParser.ONLY_UNARY_OPERATIONS, 0)

        def UNARY_OR_BINARY_OPERATIONS(self):
            return self.getToken(jjParser.UNARY_OR_BINARY_OPERATIONS, 0)

        def getRuleIndex(self):
            return jjParser.RULE_all_unary_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAll_unary_operations" ):
                listener.enterAll_unary_operations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAll_unary_operations" ):
                listener.exitAll_unary_operations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_unary_operations" ):
                return visitor.visitAll_unary_operations(self)
            else:
                return visitor.visitChildren(self)




    def all_unary_operations(self):

        localctx = jjParser.All_unary_operationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_all_unary_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cast_expression(self):
            return self.getTypedRuleContext(jjParser.Cast_expressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(jjParser.IdentifierContext,0)


        def expresion_in_parenthesis(self):
            return self.getTypedRuleContext(jjParser.Expresion_in_parenthesisContext,0)


        def function_call(self):
            return self.getTypedRuleContext(jjParser.Function_callContext,0)


        def all_unary_operations(self):
            return self.getTypedRuleContext(jjParser.All_unary_operationsContext,0)


        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def left_of_binary_operation(self):
            return self.getTypedRuleContext(jjParser.Left_of_binary_operationContext,0)


        def all_binary_operations(self):
            return self.getTypedRuleContext(jjParser.All_binary_operationsContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = jjParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expresion)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.cast_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.expresion_in_parenthesis()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.all_unary_operations()
                self.state = 240
                self.expresion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 242
                self.left_of_binary_operation()
                self.state = 243
                self.all_binary_operations()
                self.state = 244
                self.expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def PARENTHESES_BEGIN(self):
            return self.getToken(jjParser.PARENTHESES_BEGIN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(jjParser.ExpresionContext,i)


        def PARENTHESES_END(self):
            return self.getToken(jjParser.PARENTHESES_END, 0)

        def COMMA_TOKEN(self, i:int=None):
            if i is None:
                return self.getTokens(jjParser.COMMA_TOKEN)
            else:
                return self.getToken(jjParser.COMMA_TOKEN, i)

        def getRuleIndex(self):
            return jjParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = jjParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(jjParser.NAME)
            self.state = 249
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 250
            self.expresion()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 251
                self.match(jjParser.COMMA_TOKEN)
                self.state = 252
                self.expresion()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(jjParser.PARENTHESES_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(jjParser.ValueContext,0)


        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def getRuleIndex(self):
            return jjParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = jjParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_identifier)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.value()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(jjParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TYPE(self):
            return self.getToken(jjParser.NUMBER_TYPE, 0)

        def BOOL(self):
            return self.getToken(jjParser.BOOL, 0)

        def getRuleIndex(self):
            return jjParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = jjParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statement_startContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_DECL(self):
            return self.getToken(jjParser.IF_DECL, 0)

        def expresion_in_parenthesis(self):
            return self.getTypedRuleContext(jjParser.Expresion_in_parenthesisContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_if_statement_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement_start" ):
                listener.enterIf_statement_start(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement_start" ):
                listener.exitIf_statement_start(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement_start" ):
                return visitor.visitIf_statement_start(self)
            else:
                return visitor.visitChildren(self)




    def if_statement_start(self):

        localctx = jjParser.If_statement_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_statement_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(jjParser.IF_DECL)
            self.state = 267
            self.expresion_in_parenthesis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement_start(self):
            return self.getTypedRuleContext(jjParser.If_statement_startContext,0)


        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(jjParser.Else_statementContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = jjParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.if_statement_start()
            self.state = 270
            self.structural_block()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 271
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_DECL(self):
            return self.getToken(jjParser.ELSE_DECL, 0)

        def if_statement(self):
            return self.getTypedRuleContext(jjParser.If_statementContext,0)


        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = jjParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(jjParser.ELSE_DECL)
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 275
                self.if_statement()
                pass
            elif token in [13]:
                self.state = 276
                self.structural_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_DECL(self):
            return self.getToken(jjParser.WHILE_DECL, 0)

        def expresion_in_parenthesis(self):
            return self.getTypedRuleContext(jjParser.Expresion_in_parenthesisContext,0)


        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = jjParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(jjParser.WHILE_DECL)
            self.state = 280
            self.expresion_in_parenthesis()
            self.state = 281
            self.structural_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_DECL(self):
            return self.getToken(jjParser.FOR_DECL, 0)

        def PARENTHESES_BEGIN(self):
            return self.getToken(jjParser.PARENTHESES_BEGIN, 0)

        def instruction_line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jjParser.Instruction_lineContext)
            else:
                return self.getTypedRuleContext(jjParser.Instruction_lineContext,i)


        def instruction(self):
            return self.getTypedRuleContext(jjParser.InstructionContext,0)


        def PARENTHESES_END(self):
            return self.getToken(jjParser.PARENTHESES_END, 0)

        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = jjParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(jjParser.FOR_DECL)
            self.state = 284
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 285
            self.instruction_line()
            self.state = 286
            self.instruction_line()
            self.state = 287
            self.instruction()
            self.state = 288
            self.match(jjParser.PARENTHESES_END)
            self.state = 289
            self.structural_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignmnet_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(jjParser.NAME, 0)

        def ASSIGNMENT_TOKEN(self):
            return self.getToken(jjParser.ASSIGNMENT_TOKEN, 0)

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def getRuleIndex(self):
            return jjParser.RULE_assignmnet_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmnet_statement" ):
                listener.enterAssignmnet_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmnet_statement" ):
                listener.exitAssignmnet_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmnet_statement" ):
                return visitor.visitAssignmnet_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignmnet_statement(self):

        localctx = jjParser.Assignmnet_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignmnet_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(jjParser.NAME)
            self.state = 292
            self.match(jjParser.ASSIGNMENT_TOKEN)
            self.state = 293
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





