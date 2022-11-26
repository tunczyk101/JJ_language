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
        4,1,28,275,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,3,1,73,8,1,1,2,1,2,3,2,77,8,2,1,2,1,2,3,2,
        81,8,2,1,2,1,2,1,3,1,3,3,3,87,8,3,1,3,1,3,3,3,91,8,3,1,3,3,3,94,
        8,3,1,3,3,3,97,8,3,1,4,3,4,100,8,4,1,4,3,4,103,8,4,1,4,3,4,106,8,
        4,1,4,3,4,109,8,4,1,4,3,4,112,8,4,1,4,3,4,115,8,4,1,4,3,4,118,8,
        4,1,5,3,5,121,8,5,1,5,1,5,1,6,3,6,126,8,6,1,6,1,6,3,6,130,8,6,1,
        6,1,6,1,7,1,7,3,7,136,8,7,1,7,1,7,5,7,140,8,7,10,7,12,7,143,9,7,
        1,7,3,7,146,8,7,1,8,1,8,5,8,150,8,8,10,8,12,8,153,9,8,1,8,1,8,1,
        9,1,9,3,9,159,8,9,1,9,1,9,1,10,1,10,3,10,165,8,10,1,10,1,10,1,11,
        4,11,170,8,11,11,11,12,11,171,1,11,3,11,175,8,11,1,11,3,11,178,8,
        11,1,12,1,12,3,12,182,8,12,1,12,1,12,1,12,1,12,1,12,1,13,3,13,190,
        8,13,1,13,1,13,1,14,1,14,1,14,3,14,197,8,14,1,15,1,15,1,15,3,15,
        202,8,15,1,16,1,16,1,16,3,16,207,8,16,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,3,18,216,8,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,3,21,232,8,21,1,22,1,22,1,22,1,22,1,
        22,1,23,1,23,3,23,241,8,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,
        26,3,26,251,8,26,1,27,1,27,3,27,255,8,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,0,3,2,0,17,17,19,19,1,0,17,18,
        1,0,5,6,287,0,65,1,0,0,0,2,72,1,0,0,0,4,74,1,0,0,0,6,84,1,0,0,0,
        8,99,1,0,0,0,10,120,1,0,0,0,12,125,1,0,0,0,14,133,1,0,0,0,16,147,
        1,0,0,0,18,156,1,0,0,0,20,162,1,0,0,0,22,177,1,0,0,0,24,179,1,0,
        0,0,26,189,1,0,0,0,28,196,1,0,0,0,30,201,1,0,0,0,32,206,1,0,0,0,
        34,208,1,0,0,0,36,215,1,0,0,0,38,217,1,0,0,0,40,219,1,0,0,0,42,231,
        1,0,0,0,44,233,1,0,0,0,46,240,1,0,0,0,48,242,1,0,0,0,50,244,1,0,
        0,0,52,247,1,0,0,0,54,252,1,0,0,0,56,258,1,0,0,0,58,262,1,0,0,0,
        60,270,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,
        0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,3,6,3,0,69,
        1,1,0,0,0,70,73,5,2,0,0,71,73,3,4,2,0,72,70,1,0,0,0,72,71,1,0,0,
        0,73,3,1,0,0,0,74,76,5,7,0,0,75,77,5,2,0,0,76,75,1,0,0,0,76,77,1,
        0,0,0,77,78,1,0,0,0,78,80,5,28,0,0,79,81,5,2,0,0,80,79,1,0,0,0,80,
        81,1,0,0,0,81,82,1,0,0,0,82,83,3,8,4,0,83,5,1,0,0,0,84,86,5,7,0,
        0,85,87,5,2,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,90,
        5,8,0,0,89,91,5,2,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,
        92,94,3,16,8,0,93,92,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,5,
        2,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,7,1,0,0,0,98,100,3,14,7,0,99,
        98,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,103,5,2,0,0,102,101,
        1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,106,3,20,10,0,105,104,
        1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,109,5,2,0,0,108,107,
        1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,112,3,16,8,0,111,110,
        1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,115,5,2,0,0,114,113,
        1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,3,18,9,0,117,116,
        1,0,0,0,117,118,1,0,0,0,118,9,1,0,0,0,119,121,5,10,0,0,120,119,1,
        0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,28,0,0,123,11,1,
        0,0,0,124,126,5,2,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,1,
        0,0,0,127,129,5,12,0,0,128,130,5,2,0,0,129,128,1,0,0,0,129,130,1,
        0,0,0,130,131,1,0,0,0,131,132,3,10,5,0,132,13,1,0,0,0,133,135,5,
        22,0,0,134,136,5,2,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,
        0,0,0,137,141,3,10,5,0,138,140,3,12,6,0,139,138,1,0,0,0,140,143,
        1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,144,146,5,2,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,15,1,
        0,0,0,147,151,5,13,0,0,148,150,3,22,11,0,149,148,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,151,
        1,0,0,0,154,155,5,14,0,0,155,17,1,0,0,0,156,158,5,21,0,0,157,159,
        5,2,0,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,161,
        3,42,21,0,161,19,1,0,0,0,162,164,5,23,0,0,163,165,5,2,0,0,164,163,
        1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,3,42,21,0,167,21,
        1,0,0,0,168,170,3,28,14,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,175,5,2,0,0,174,173,
        1,0,0,0,174,175,1,0,0,0,175,178,1,0,0,0,176,178,5,2,0,0,177,169,
        1,0,0,0,177,176,1,0,0,0,178,23,1,0,0,0,179,181,5,9,0,0,180,182,5,
        10,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,184,5,
        28,0,0,184,185,5,13,0,0,185,186,3,42,21,0,186,187,5,14,0,0,187,25,
        1,0,0,0,188,190,3,32,16,0,189,188,1,0,0,0,189,190,1,0,0,0,190,191,
        1,0,0,0,191,192,5,11,0,0,192,27,1,0,0,0,193,197,3,26,13,0,194,197,
        3,30,15,0,195,197,3,16,8,0,196,193,1,0,0,0,196,194,1,0,0,0,196,195,
        1,0,0,0,197,29,1,0,0,0,198,202,3,56,28,0,199,202,3,52,26,0,200,202,
        3,58,29,0,201,198,1,0,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,31,
        1,0,0,0,203,207,3,24,12,0,204,207,3,60,30,0,205,207,3,42,21,0,206,
        203,1,0,0,0,206,204,1,0,0,0,206,205,1,0,0,0,207,33,1,0,0,0,208,209,
        5,15,0,0,209,210,3,42,21,0,210,211,5,16,0,0,211,35,1,0,0,0,212,216,
        3,46,23,0,213,216,3,34,17,0,214,216,3,44,22,0,215,212,1,0,0,0,215,
        213,1,0,0,0,215,214,1,0,0,0,216,37,1,0,0,0,217,218,7,0,0,0,218,39,
        1,0,0,0,219,220,7,1,0,0,220,41,1,0,0,0,221,232,3,46,23,0,222,232,
        3,34,17,0,223,232,3,44,22,0,224,225,3,40,20,0,225,226,3,42,21,0,
        226,232,1,0,0,0,227,228,3,36,18,0,228,229,3,38,19,0,229,230,3,42,
        21,0,230,232,1,0,0,0,231,221,1,0,0,0,231,222,1,0,0,0,231,223,1,0,
        0,0,231,224,1,0,0,0,231,227,1,0,0,0,232,43,1,0,0,0,233,234,5,28,
        0,0,234,235,5,15,0,0,235,236,3,42,21,0,236,237,5,16,0,0,237,45,1,
        0,0,0,238,241,3,48,24,0,239,241,5,28,0,0,240,238,1,0,0,0,240,239,
        1,0,0,0,241,47,1,0,0,0,242,243,7,2,0,0,243,49,1,0,0,0,244,245,5,
        24,0,0,245,246,3,34,17,0,246,51,1,0,0,0,247,248,3,50,25,0,248,250,
        3,16,8,0,249,251,3,54,27,0,250,249,1,0,0,0,250,251,1,0,0,0,251,53,
        1,0,0,0,252,254,5,25,0,0,253,255,3,50,25,0,254,253,1,0,0,0,254,255,
        1,0,0,0,255,256,1,0,0,0,256,257,3,16,8,0,257,55,1,0,0,0,258,259,
        5,26,0,0,259,260,3,34,17,0,260,261,3,16,8,0,261,57,1,0,0,0,262,263,
        5,27,0,0,263,264,5,15,0,0,264,265,3,26,13,0,265,266,3,26,13,0,266,
        267,3,32,16,0,267,268,5,16,0,0,268,269,3,16,8,0,269,59,1,0,0,0,270,
        271,5,28,0,0,271,272,5,20,0,0,272,273,3,42,21,0,273,61,1,0,0,0,37,
        65,72,76,80,86,90,93,96,99,102,105,108,111,114,117,120,125,129,135,
        141,145,151,158,164,171,174,177,181,189,196,201,206,215,231,240,
        250,254
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
                     "'with'", "'when'", "'if'", "'else'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_START", "COMMENT", "WS", "NEW_LINE", 
                      "NUMBER_TYPE", "BOOL", "FUNC_DECL", "MAIN_FUNC_NAME", 
                      "VARIABLE_TOKEN", "MUTABLE_TOKEN", "END_OF_INSTRUCTION", 
                      "COMMA_TOKEN", "BLOCK_BEGIN", "BLOCK_END", "PARENTHESES_BEGIN", 
                      "PARENTHESES_END", "UNARY_OR_BINARY_OPERATIONS", "ONLY_UNARY_OPERATIONS", 
                      "ONLY_BINARY_OPERATIONS", "ASSIGNMENT_TOKEN", "RETURN_DECL", 
                      "WITH_DECL", "WHEN_DECL", "IF_DECL", "ELSE_DECL", 
                      "WHILE_DECL", "FOR_DECL", "NAME" ]

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
    RULE_left_of_binary_operation = 18
    RULE_all_binary_operations = 19
    RULE_all_unary_operations = 20
    RULE_expresion = 21
    RULE_function_call = 22
    RULE_identifier = 23
    RULE_value = 24
    RULE_if_statement_start = 25
    RULE_if_statement = 26
    RULE_else_statement = 27
    RULE_while_statement = 28
    RULE_for_statement = 29
    RULE_assignmnet_statement = 30

    ruleNames =  [ "prog", "global_line", "function", "function_main", "optinal_function_blocks", 
                   "argument_decl", "additional_arguments_decl", "arguments_block", 
                   "structural_block", "return_block", "guard_block", "structural_line", 
                   "variable_declaration", "instruction_line", "structural_line_instruction", 
                   "statement", "instruction", "expresion_in_parenthesis", 
                   "left_of_binary_operation", "all_binary_operations", 
                   "all_unary_operations", "expresion", "function_call", 
                   "identifier", "value", "if_statement_start", "if_statement", 
                   "else_statement", "while_statement", "for_statement", 
                   "assignmnet_statement" ]

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
    NAME=28

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
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.global_line() 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 68
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(jjParser.COMMENT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
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
            self.state = 74
            self.match(jjParser.FUNC_DECL)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 75
                self.match(jjParser.COMMENT)


            self.state = 78
            self.match(jjParser.NAME)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(jjParser.COMMENT)


            self.state = 82
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
            self.state = 84
            self.match(jjParser.FUNC_DECL)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 85
                self.match(jjParser.COMMENT)


            self.state = 88
            self.match(jjParser.MAIN_FUNC_NAME)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(jjParser.COMMENT)


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 92
                self.structural_block()


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 95
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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 98
                self.arguments_block()


            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 101
                self.match(jjParser.COMMENT)


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 104
                self.guard_block()


            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(jjParser.COMMENT)


            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 110
                self.structural_block()


            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 113
                self.match(jjParser.COMMENT)


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 116
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
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 119
                self.match(jjParser.MUTABLE_TOKEN)


            self.state = 122
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
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 124
                self.match(jjParser.COMMENT)


            self.state = 127
            self.match(jjParser.COMMA_TOKEN)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 128
                self.match(jjParser.COMMENT)


            self.state = 131
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
            self.state = 133
            self.match(jjParser.WITH_DECL)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 134
                self.match(jjParser.COMMENT)


            self.state = 137
            self.argument_decl()
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    self.additional_arguments_decl() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 144
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
            self.state = 147
            self.match(jjParser.BLOCK_BEGIN)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 486976100) != 0:
                self.state = 148
                self.structural_line()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
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
            self.state = 156
            self.match(jjParser.RETURN_DECL)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 157
                self.match(jjParser.COMMENT)


            self.state = 160
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
            self.state = 162
            self.match(jjParser.WHEN_DECL)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 163
                self.match(jjParser.COMMENT)


            self.state = 166
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
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 9, 11, 13, 15, 17, 18, 24, 26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 168
                        self.structural_line_instruction()

                    else:
                        raise NoViableAltException(self)
                    self.state = 171 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 173
                    self.match(jjParser.COMMENT)


                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
            self.state = 179
            self.match(jjParser.VARIABLE_TOKEN)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 180
                self.match(jjParser.MUTABLE_TOKEN)


            self.state = 183
            self.match(jjParser.NAME)
            self.state = 184
            self.match(jjParser.BLOCK_BEGIN)
            self.state = 185
            self.expresion()
            self.state = 186
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
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 268862048) != 0:
                self.state = 188
                self.instruction()


            self.state = 191
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
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 9, 11, 15, 17, 18, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.instruction_line()
                pass
            elif token in [24, 26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.statement()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.while_statement()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.if_statement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.assignmnet_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
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
            self.state = 208
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 209
            self.expresion()
            self.state = 210
            self.match(jjParser.PARENTHESES_END)
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
        self.enterRule(localctx, 36, self.RULE_left_of_binary_operation)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.expresion_in_parenthesis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
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
        self.enterRule(localctx, 38, self.RULE_all_binary_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
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
        self.enterRule(localctx, 40, self.RULE_all_unary_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
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
        self.enterRule(localctx, 42, self.RULE_expresion)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.expresion_in_parenthesis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.all_unary_operations()
                self.state = 225
                self.expresion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.left_of_binary_operation()
                self.state = 228
                self.all_binary_operations()
                self.state = 229
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

        def expresion(self):
            return self.getTypedRuleContext(jjParser.ExpresionContext,0)


        def PARENTHESES_END(self):
            return self.getToken(jjParser.PARENTHESES_END, 0)

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
        self.enterRule(localctx, 44, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(jjParser.NAME)
            self.state = 234
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 235
            self.expresion()
            self.state = 236
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
        self.enterRule(localctx, 46, self.RULE_identifier)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.value()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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
        self.enterRule(localctx, 48, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
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
        self.enterRule(localctx, 50, self.RULE_if_statement_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(jjParser.IF_DECL)
            self.state = 245
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
        self.enterRule(localctx, 52, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.if_statement_start()
            self.state = 248
            self.structural_block()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 249
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

        def structural_block(self):
            return self.getTypedRuleContext(jjParser.Structural_blockContext,0)


        def if_statement_start(self):
            return self.getTypedRuleContext(jjParser.If_statement_startContext,0)


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
        self.enterRule(localctx, 54, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(jjParser.ELSE_DECL)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 253
                self.if_statement_start()


            self.state = 256
            self.structural_block()
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
        self.enterRule(localctx, 56, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(jjParser.WHILE_DECL)
            self.state = 259
            self.expresion_in_parenthesis()
            self.state = 260
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
        self.enterRule(localctx, 58, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(jjParser.FOR_DECL)
            self.state = 263
            self.match(jjParser.PARENTHESES_BEGIN)
            self.state = 264
            self.instruction_line()
            self.state = 265
            self.instruction_line()
            self.state = 266
            self.instruction()
            self.state = 267
            self.match(jjParser.PARENTHESES_END)
            self.state = 268
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
        self.enterRule(localctx, 60, self.RULE_assignmnet_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(jjParser.NAME)
            self.state = 271
            self.match(jjParser.ASSIGNMENT_TOKEN)
            self.state = 272
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





