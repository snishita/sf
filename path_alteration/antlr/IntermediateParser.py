# Generated from Intermediate.g4 by ANTLR 4.11.1
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
        4,1,27,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,5,1,26,8,1,
        10,1,12,1,29,9,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,44,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,1,5,3,5,59,8,5,1,6,1,6,1,6,3,6,64,8,6,1,6,0,0,7,0,2,4,6,8,10,12,
        0,6,1,0,3,5,1,0,13,14,1,0,7,9,1,0,17,21,1,0,15,16,1,0,11,12,69,0,
        17,1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,47,1,0,0,0,8,52,1,0,0,0,10,
        58,1,0,0,0,12,63,1,0,0,0,14,15,3,2,1,0,15,16,5,26,0,0,16,18,1,0,
        0,0,17,14,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,
        1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,35,3,4,2,0,24,26,3,8,4,0,25,
        24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,
        0,29,27,1,0,0,0,30,36,7,0,0,0,31,32,7,1,0,0,32,36,5,10,0,0,33,36,
        5,1,0,0,34,36,5,2,0,0,35,27,1,0,0,0,35,31,1,0,0,0,35,33,1,0,0,0,
        35,34,1,0,0,0,36,37,1,0,0,0,37,38,3,6,3,0,38,44,1,0,0,0,39,40,5,
        6,0,0,40,44,3,6,3,0,41,42,7,2,0,0,42,44,3,6,3,0,43,23,1,0,0,0,43,
        39,1,0,0,0,43,41,1,0,0,0,44,3,1,0,0,0,45,46,7,3,0,0,46,5,1,0,0,0,
        47,48,3,10,5,0,48,49,3,12,6,0,49,50,3,4,2,0,50,51,7,4,0,0,51,7,1,
        0,0,0,52,53,7,5,0,0,53,54,3,6,3,0,54,9,1,0,0,0,55,59,5,22,0,0,56,
        59,5,23,0,0,57,59,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,
        0,0,59,11,1,0,0,0,60,64,5,24,0,0,61,64,5,25,0,0,62,64,1,0,0,0,63,
        60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,13,1,0,0,0,6,19,27,35,
        43,58,63
    ]

class IntermediateParser ( Parser ):

    grammarFileName = "Intermediate.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'pu-rl'", "'pu-lr'", "'pu-r'", "'pu-l'", 
                     "'pu'", "'up'", "'re'", "'re-l'", "'re-r'", "'tw'", 
                     "'mo'", "'mu'", "'ma'", "'mt'", "'S'", "'N'", "'T'", 
                     "'F'", "'M'", "'R'", "'L'", "'t'", "'b'", "'n'", "'f'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "PURL", "PULR", "PUR", "PUL", "PU", "UP", 
                      "RE", "REL", "RER", "TW", "MO", "MU", "MA", "MT", 
                      "S", "N", "T", "F", "M", "R", "L", "HT", "HB", "DN", 
                      "DF", "SEMICOLON", "WS" ]

    RULE_intermediate = 0
    RULE_command = 1
    RULE_finger = 2
    RULE_string = 3
    RULE_move = 4
    RULE_tb = 5
    RULE_nf = 6

    ruleNames =  [ "intermediate", "command", "finger", "string", "move", 
                   "tb", "nf" ]

    EOF = Token.EOF
    PURL=1
    PULR=2
    PUR=3
    PUL=4
    PU=5
    UP=6
    RE=7
    REL=8
    RER=9
    TW=10
    MO=11
    MU=12
    MA=13
    MT=14
    S=15
    N=16
    T=17
    F=18
    M=19
    R=20
    L=21
    HT=22
    HB=23
    DN=24
    DF=25
    SEMICOLON=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IntermediateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IntermediateParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IntermediateParser.CommandContext)
            else:
                return self.getTypedRuleContext(IntermediateParser.CommandContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(IntermediateParser.SEMICOLON)
            else:
                return self.getToken(IntermediateParser.SEMICOLON, i)

        def getRuleIndex(self):
            return IntermediateParser.RULE_intermediate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntermediate" ):
                listener.enterIntermediate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntermediate" ):
                listener.exitIntermediate(self)




    def intermediate(self):

        localctx = IntermediateParser.IntermediateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_intermediate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.command()
                self.state = 15
                self.match(IntermediateParser.SEMICOLON)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 4064192) != 0):
                    break

            self.state = 21
            self.match(IntermediateParser.EOF)
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

        def finger(self):
            return self.getTypedRuleContext(IntermediateParser.FingerContext,0)


        def string(self):
            return self.getTypedRuleContext(IntermediateParser.StringContext,0)


        def TW(self):
            return self.getToken(IntermediateParser.TW, 0)

        def PURL(self):
            return self.getToken(IntermediateParser.PURL, 0)

        def PULR(self):
            return self.getToken(IntermediateParser.PULR, 0)

        def PU(self):
            return self.getToken(IntermediateParser.PU, 0)

        def PUR(self):
            return self.getToken(IntermediateParser.PUR, 0)

        def PUL(self):
            return self.getToken(IntermediateParser.PUL, 0)

        def MA(self):
            return self.getToken(IntermediateParser.MA, 0)

        def MT(self):
            return self.getToken(IntermediateParser.MT, 0)

        def move(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IntermediateParser.MoveContext)
            else:
                return self.getTypedRuleContext(IntermediateParser.MoveContext,i)


        def UP(self):
            return self.getToken(IntermediateParser.UP, 0)

        def RE(self):
            return self.getToken(IntermediateParser.RE, 0)

        def REL(self):
            return self.getToken(IntermediateParser.REL, 0)

        def RER(self):
            return self.getToken(IntermediateParser.RER, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = IntermediateParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.finger()
                self.state = 35
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5, 11, 12]:
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==11 or _la==12:
                        self.state = 24
                        self.move()
                        self.state = 29
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 30
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                elif token in [13, 14]:
                    self.state = 31
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 32
                    self.match(IntermediateParser.TW)
                    pass
                elif token in [1]:
                    self.state = 33
                    self.match(IntermediateParser.PURL)
                    pass
                elif token in [2]:
                    self.state = 34
                    self.match(IntermediateParser.PULR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 37
                self.string()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(IntermediateParser.UP)
                self.state = 40
                self.string()
                pass
            elif token in [7, 8, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                self.string()
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
            return self.getToken(IntermediateParser.T, 0)

        def F(self):
            return self.getToken(IntermediateParser.F, 0)

        def M(self):
            return self.getToken(IntermediateParser.M, 0)

        def R(self):
            return self.getToken(IntermediateParser.R, 0)

        def L(self):
            return self.getToken(IntermediateParser.L, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_finger

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinger" ):
                listener.enterFinger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinger" ):
                listener.exitFinger(self)




    def finger(self):

        localctx = IntermediateParser.FingerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_finger)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4063232) != 0):
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


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tb(self):
            return self.getTypedRuleContext(IntermediateParser.TbContext,0)


        def nf(self):
            return self.getTypedRuleContext(IntermediateParser.NfContext,0)


        def finger(self):
            return self.getTypedRuleContext(IntermediateParser.FingerContext,0)


        def S(self):
            return self.getToken(IntermediateParser.S, 0)

        def N(self):
            return self.getToken(IntermediateParser.N, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = IntermediateParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.tb()
            self.state = 48
            self.nf()
            self.state = 49
            self.finger()
            self.state = 50
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(IntermediateParser.StringContext,0)


        def MO(self):
            return self.getToken(IntermediateParser.MO, 0)

        def MU(self):
            return self.getToken(IntermediateParser.MU, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)




    def move(self):

        localctx = IntermediateParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_move)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 53
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
            return self.getToken(IntermediateParser.HT, 0)

        def HB(self):
            return self.getToken(IntermediateParser.HB, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_tb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTb" ):
                listener.enterTb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTb" ):
                listener.exitTb(self)




    def tb(self):

        localctx = IntermediateParser.TbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tb)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(IntermediateParser.HT)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(IntermediateParser.HB)
                pass
            elif token in [17, 18, 19, 20, 21, 24, 25]:
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
            return self.getToken(IntermediateParser.DN, 0)

        def DF(self):
            return self.getToken(IntermediateParser.DF, 0)

        def getRuleIndex(self):
            return IntermediateParser.RULE_nf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNf" ):
                listener.enterNf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNf" ):
                listener.exitNf(self)




    def nf(self):

        localctx = IntermediateParser.NfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nf)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(IntermediateParser.DN)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(IntermediateParser.DF)
                pass
            elif token in [17, 18, 19, 20, 21]:
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





