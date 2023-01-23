# Generated from Intermediate.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IntermediateParser import IntermediateParser
else:
    from IntermediateParser import IntermediateParser

# This class defines a complete listener for a parse tree produced by IntermediateParser.
class IntermediateListener(ParseTreeListener):

    # Enter a parse tree produced by IntermediateParser#intermediate.
    def enterIntermediate(self, ctx:IntermediateParser.IntermediateContext):
        pass

    # Exit a parse tree produced by IntermediateParser#intermediate.
    def exitIntermediate(self, ctx:IntermediateParser.IntermediateContext):
        pass


    # Enter a parse tree produced by IntermediateParser#command.
    def enterCommand(self, ctx:IntermediateParser.CommandContext):
        pass

    # Exit a parse tree produced by IntermediateParser#command.
    def exitCommand(self, ctx:IntermediateParser.CommandContext):
        pass


    # Enter a parse tree produced by IntermediateParser#finger.
    def enterFinger(self, ctx:IntermediateParser.FingerContext):
        pass

    # Exit a parse tree produced by IntermediateParser#finger.
    def exitFinger(self, ctx:IntermediateParser.FingerContext):
        pass


    # Enter a parse tree produced by IntermediateParser#string.
    def enterString(self, ctx:IntermediateParser.StringContext):
        pass

    # Exit a parse tree produced by IntermediateParser#string.
    def exitString(self, ctx:IntermediateParser.StringContext):
        pass


    # Enter a parse tree produced by IntermediateParser#move.
    def enterMove(self, ctx:IntermediateParser.MoveContext):
        pass

    # Exit a parse tree produced by IntermediateParser#move.
    def exitMove(self, ctx:IntermediateParser.MoveContext):
        pass


    # Enter a parse tree produced by IntermediateParser#tb.
    def enterTb(self, ctx:IntermediateParser.TbContext):
        pass

    # Exit a parse tree produced by IntermediateParser#tb.
    def exitTb(self, ctx:IntermediateParser.TbContext):
        pass


    # Enter a parse tree produced by IntermediateParser#nf.
    def enterNf(self, ctx:IntermediateParser.NfContext):
        pass

    # Exit a parse tree produced by IntermediateParser#nf.
    def exitNf(self, ctx:IntermediateParser.NfContext):
        pass



del IntermediateParser