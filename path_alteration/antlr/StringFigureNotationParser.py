# Generated from StringFigureNotation.g4 by ANTLR 4.11.1
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
        4,1,26,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,1,1,1,1,3,1,37,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,3,1,3,1,3,3,3,54,8,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,66,8,5,1,5,1,5,1,6,1,6,
        1,6,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,8,3,8,81,8,8,1,8,0,0,9,0,2,
        4,6,8,10,12,14,16,0,4,1,0,9,10,1,0,14,18,1,0,12,13,2,0,7,8,11,11,
        88,0,23,1,0,0,0,2,46,1,0,0,0,4,48,1,0,0,0,6,53,1,0,0,0,8,57,1,0,
        0,0,10,65,1,0,0,0,12,69,1,0,0,0,14,75,1,0,0,0,16,80,1,0,0,0,18,19,
        3,2,1,0,19,20,5,25,0,0,20,22,1,0,0,0,21,18,1,0,0,0,22,25,1,0,0,0,
        23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,0,26,36,3,6,
        3,0,27,29,3,12,6,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,
        31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,37,5,1,0,0,34,35,7,0,0,
        0,35,37,5,6,0,0,36,30,1,0,0,0,36,34,1,0,0,0,37,38,1,0,0,0,38,39,
        3,10,5,0,39,47,1,0,0,0,40,41,5,2,0,0,41,47,3,8,4,0,42,43,5,3,0,0,
        43,47,3,10,5,0,44,47,5,4,0,0,45,47,5,5,0,0,46,26,1,0,0,0,46,40,1,
        0,0,0,46,42,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,
        49,7,1,0,0,49,5,1,0,0,0,50,54,5,23,0,0,51,54,5,24,0,0,52,54,1,0,
        0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,56,
        3,4,2,0,56,7,1,0,0,0,57,58,3,14,7,0,58,59,3,16,8,0,59,60,3,4,2,0,
        60,61,7,2,0,0,61,9,1,0,0,0,62,66,5,23,0,0,63,66,5,24,0,0,64,66,1,
        0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,
        68,3,8,4,0,68,11,1,0,0,0,69,70,7,3,0,0,70,71,3,8,4,0,71,13,1,0,0,
        0,72,76,5,19,0,0,73,76,5,20,0,0,74,76,1,0,0,0,75,72,1,0,0,0,75,73,
        1,0,0,0,75,74,1,0,0,0,76,15,1,0,0,0,77,81,5,21,0,0,78,81,5,22,0,
        0,79,81,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,17,
        1,0,0,0,8,23,30,36,46,53,65,75,80
    ]

class StringFigureNotationParser ( Parser ):

    grammarFileName = "StringFigureNotation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pu'", "'up'", "'re'", "'OE'", "'NE'", 
                     "'tw'", "'mo'", "'mu'", "'ma'", "'mt'", "'th'", "'S'", 
                     "'N'", "'T'", "'F'", "'M'", "'R'", "'L'", "'t'", "'b'", 
                     "'n'", "'f'", "'l'", "'r'", "';'" ]

    symbolicNames = [ "<INVALID>", "PU", "UP", "RE", "OE", "NE", "TW", "MO", 
                      "MU", "MA", "MT", "TH", "S", "N", "T", "F", "M", "R", 
                      "L", "HT", "HB", "DN", "DF", "SIDEL", "SIDER", "SEMICOLON", 
                      "WS" ]

    RULE_commands = 0
    RULE_command = 1
    RULE_finger = 2
    RULE_fingerWithSide = 3
    RULE_string = 4
    RULE_stringWithSide = 5
    RULE_move = 6
    RULE_tb = 7
    RULE_nf = 8

    ruleNames =  [ "commands", "command", "finger", "fingerWithSide", "string", 
                   "stringWithSide", "move", "tb", "nf" ]

    EOF = Token.EOF
    PU=1
    UP=2
    RE=3
    OE=4
    NE=5
    TW=6
    MO=7
    MU=8
    MA=9
    MT=10
    TH=11
    S=12
    N=13
    T=14
    F=15
    M=16
    R=17
    L=18
    HT=19
    HB=20
    DN=21
    DF=22
    SIDEL=23
    SIDER=24
    SEMICOLON=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StringFigureNotationParser.CommandContext)
            else:
                return self.getTypedRuleContext(StringFigureNotationParser.CommandContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(StringFigureNotationParser.SEMICOLON)
            else:
                return self.getToken(StringFigureNotationParser.SEMICOLON, i)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)




    def commands(self):

        localctx = StringFigureNotationParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 25673788) != 0:
                self.state = 18
                self.command()
                self.state = 19
                self.match(StringFigureNotationParser.SEMICOLON)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fingerWithSide(self):
            return self.getTypedRuleContext(StringFigureNotationParser.FingerWithSideContext,0)


        def stringWithSide(self):
            return self.getTypedRuleContext(StringFigureNotationParser.StringWithSideContext,0)


        def PU(self):
            return self.getToken(StringFigureNotationParser.PU, 0)

        def TW(self):
            return self.getToken(StringFigureNotationParser.TW, 0)

        def MA(self):
            return self.getToken(StringFigureNotationParser.MA, 0)

        def MT(self):
            return self.getToken(StringFigureNotationParser.MT, 0)

        def move(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StringFigureNotationParser.MoveContext)
            else:
                return self.getTypedRuleContext(StringFigureNotationParser.MoveContext,i)


        def UP(self):
            return self.getToken(StringFigureNotationParser.UP, 0)

        def string(self):
            return self.getTypedRuleContext(StringFigureNotationParser.StringContext,0)


        def RE(self):
            return self.getToken(StringFigureNotationParser.RE, 0)

        def OE(self):
            return self.getToken(StringFigureNotationParser.OE, 0)

        def NE(self):
            return self.getToken(StringFigureNotationParser.NE, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = StringFigureNotationParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 17, 18, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.fingerWithSide()
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 7, 8, 11]:
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2432) != 0:
                        self.state = 27
                        self.move()
                        self.state = 32
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 33
                    self.match(StringFigureNotationParser.PU)
                    pass
                elif token in [9, 10]:
                    self.state = 34
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==10):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 35
                    self.match(StringFigureNotationParser.TW)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self.stringWithSide()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(StringFigureNotationParser.UP)
                self.state = 41
                self.string()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(StringFigureNotationParser.RE)
                self.state = 43
                self.stringWithSide()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.match(StringFigureNotationParser.OE)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.match(StringFigureNotationParser.NE)
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


    class FingerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T(self):
            return self.getToken(StringFigureNotationParser.T, 0)

        def F(self):
            return self.getToken(StringFigureNotationParser.F, 0)

        def M(self):
            return self.getToken(StringFigureNotationParser.M, 0)

        def R(self):
            return self.getToken(StringFigureNotationParser.R, 0)

        def L(self):
            return self.getToken(StringFigureNotationParser.L, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_finger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinger" ):
                listener.enterFinger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinger" ):
                listener.exitFinger(self)




    def finger(self):

        localctx = StringFigureNotationParser.FingerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_finger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 507904) != 0):
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


    class FingerWithSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def finger(self):
            return self.getTypedRuleContext(StringFigureNotationParser.FingerContext,0)


        def SIDEL(self):
            return self.getToken(StringFigureNotationParser.SIDEL, 0)

        def SIDER(self):
            return self.getToken(StringFigureNotationParser.SIDER, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_fingerWithSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFingerWithSide" ):
                listener.enterFingerWithSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFingerWithSide" ):
                listener.exitFingerWithSide(self)




    def fingerWithSide(self):

        localctx = StringFigureNotationParser.FingerWithSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fingerWithSide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 50
                self.match(StringFigureNotationParser.SIDEL)
                pass
            elif token in [24]:
                self.state = 51
                self.match(StringFigureNotationParser.SIDER)
                pass
            elif token in [14, 15, 16, 17, 18]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 55
            self.finger()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tb(self):
            return self.getTypedRuleContext(StringFigureNotationParser.TbContext,0)


        def nf(self):
            return self.getTypedRuleContext(StringFigureNotationParser.NfContext,0)


        def finger(self):
            return self.getTypedRuleContext(StringFigureNotationParser.FingerContext,0)


        def S(self):
            return self.getToken(StringFigureNotationParser.S, 0)

        def N(self):
            return self.getToken(StringFigureNotationParser.N, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = StringFigureNotationParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.tb()
            self.state = 58
            self.nf()
            self.state = 59
            self.finger()
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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


    class StringWithSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(StringFigureNotationParser.StringContext,0)


        def SIDEL(self):
            return self.getToken(StringFigureNotationParser.SIDEL, 0)

        def SIDER(self):
            return self.getToken(StringFigureNotationParser.SIDER, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_stringWithSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringWithSide" ):
                listener.enterStringWithSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringWithSide" ):
                listener.exitStringWithSide(self)




    def stringWithSide(self):

        localctx = StringFigureNotationParser.StringWithSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stringWithSide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 62
                self.match(StringFigureNotationParser.SIDEL)
                pass
            elif token in [24]:
                self.state = 63
                self.match(StringFigureNotationParser.SIDER)
                pass
            elif token in [14, 15, 16, 17, 18, 19, 20, 21, 22]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 67
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(StringFigureNotationParser.StringContext,0)


        def MO(self):
            return self.getToken(StringFigureNotationParser.MO, 0)

        def MU(self):
            return self.getToken(StringFigureNotationParser.MU, 0)

        def TH(self):
            return self.getToken(StringFigureNotationParser.TH, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)




    def move(self):

        localctx = StringFigureNotationParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_move)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 2432) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 70
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HT(self):
            return self.getToken(StringFigureNotationParser.HT, 0)

        def HB(self):
            return self.getToken(StringFigureNotationParser.HB, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_tb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTb" ):
                listener.enterTb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTb" ):
                listener.exitTb(self)




    def tb(self):

        localctx = StringFigureNotationParser.TbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tb)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(StringFigureNotationParser.HT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(StringFigureNotationParser.HB)
                pass
            elif token in [14, 15, 16, 17, 18, 21, 22]:
                self.enterOuterAlt(localctx, 3)

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


    class NfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DN(self):
            return self.getToken(StringFigureNotationParser.DN, 0)

        def DF(self):
            return self.getToken(StringFigureNotationParser.DF, 0)

        def getRuleIndex(self):
            return StringFigureNotationParser.RULE_nf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNf" ):
                listener.enterNf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNf" ):
                listener.exitNf(self)




    def nf(self):

        localctx = StringFigureNotationParser.NfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_nf)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(StringFigureNotationParser.DN)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(StringFigureNotationParser.DF)
                pass
            elif token in [14, 15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 3)

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





