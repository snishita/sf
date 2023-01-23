import sys
from antlr4 import *
from StringFigureNotationLexer import StringFigureNotationLexer
from StringFigureNotationParser import StringFigureNotationParser
from StringFigureNotationListener import StringFigureNotationListener
from Intermediate import *

class MyListener(StringFigureNotationListener):
    def __init__(self):
        self.commands = []

    def enterCommand(self, ctx:StringFigureNotationParser.CommandContext):
        # ここでリスナーを初期化
        self.fingers = []  # 指はPU の最初，string に出てくるためスタックで管理
        self.finger_side = None
        self.tb = None
        self.nf = None
        self.string = None
        self.string_side = None
        self.moves = [] # 移動は複数回実行する可能性があるので，リストで管理

    def exitFinger(self, ctx:StringFigureNotationParser.FingerContext):
        if ctx.T():
            self.fingers.append(Finger.T)
        elif ctx.F():
            self.fingers.append(Finger.F)
        elif ctx.M():
            self.fingers.append(Finger.M)
        elif ctx.R():
            self.fingers.append(Finger.R)
        else:
            self.fingers.append(Finger.L)

    def exitFingerWithSide(self, ctx:StringFigureNotationParser.FingerWithSideContext):
        if ctx.SIDEL():
            self.finger_side = Finger.L     # 左を意味．本来別のデータ型を宣言すべきだが，Finger.L で代用
        elif ctx.SIDER():
            self.finger_side = Finger.R     # 右を意味．本来別のデータ型を宣言すべきだが，Finger.R で代用
        else:
            self.finger_side = None

    def exitTb(self, ctx:StringFigureNotationParser.TbContext):
        if ctx.HT():
            self.tb = Height.t
        elif ctx.HB():
            self.tb = Height.b
        else:
            self.tb = None
    def exitNf(self, ctx:StringFigureNotationParser.NfContext):
        if ctx.DN():
            self.nf = Depth.n
        elif ctx.DF():
            self.nf = Depth.f
        else:
            self.nf = None

    def exitString(self, ctx:StringFigureNotationParser.StringContext):
        self.string = String(self.tb, self.nf, self.fingers.pop(), True if ctx.S() else False)
        self.tb = self.nf = None
        # self.fingers はpop() によって削除済み

    def exitStringWithSide(self, ctx:StringFigureNotationParser.StringWithSideContext):
        if ctx.SIDEL():
            self.string_side = Finger.L     # 左を意味．本来別のデータ型を宣言すべきだが，Finger.L で代用
        elif ctx.SIDER():
            self.string_side = Finger.R     # 右を意味．本来別のデータ型を宣言すべきだが，Finger.R で代用
        else:
            self.string_side = None
    
    def exitMove(self, ctx:StringFigureNotationParser.MoveContext):
        if ctx.MO():
            self.moves.append(Move(True, self.string))
        elif ctx.MU():
            self.moves.append(Move(False, self.string))
        else:
            if self.string.isString:
                raise ValueError('th は Noose に対してのみ実行できます')
            else:
                overUnder = True if self.fingers[0].value < self.string.finger else False
                self.moves.append(Move(overUnder, String(self.string.height, Depth.n, self.string.finger, True)))
                self.moves.append(Move(not overUnder, String(self.string.height, Depth.f, self.string.finger, True)))
        #self.moves.append(Move(True if ctx.MO() else False, self.string))
        self.string = None
    
    def exitCommand(self, ctx:StringFigureNotationParser.CommandContext):
        if ctx.UP():
            self.commands.append(IUp(self.string))
        elif ctx.RE():
            if self.string_side:
                if self.string_side == Finger.L:
                    self.commands.append(IReL(self.string))
                else:
                    self.commands.append(IReR(self.string))
            else:
                self.commands.append(IRe(self.string))
        elif ctx.OE():
            pass
        elif ctx.NE():
            self.commands.append(IUp(String(Height.b, None, Finger.F, False)))
            self.commands.append(IRe(String(Height.b, None, Finger.F, False)))
            self.commands.append(IUp(String(Height.b, None, Finger.T, False)))
            self.commands.append(IUp(String(Height.b, None, Finger.T, False)))
            self.commands.append(IRe(String(Height.b, None, Finger.T, False)))
        elif ctx.PU():
            if self.finger_side:
                if self.string_side:
                    if self.finger_side == self.string_side:
                        if self.finger_side == Finger.L:
                            self.commands.append(IPickupL(self.fingers.pop(), self.moves, self.string))
                        else:
                            self.commands.append(IPickupR(self.fingers.pop(), self.moves, self.string))
                    elif self.moves == []:
                        if self.finger_side == Finger.L:
                            self.commands.append(IPickupLR(self.fingers.pop(), self.string))
                        else:
                            self.commands.append(IPickupRL(self.fingers.pop(), self.string))
                    else:
                        raise ValueError('左右反対側のヒモを取るときには，mo/mu は指定できません．（常にほかの全てのヒモの上からとります．）')

                else:
                    raise ValueError('指の左右が指定されているので，ヒモの左右も指定してください. ')
            elif self.string_side:
                raise ValueError('ヒモの左右が指定されているので，指の左右も指定してください. ')
            else:
                self.commands.append(IPickup(self.fingers.pop(), self.moves, self.string))
        else:
            self.commands.append(ITwist(self.fingers.pop(), 
                True if ctx.MA() else False, self.string))


def main(argv):
    input = InputStream(sys.stdin.read())
    lexer = StringFigureNotationLexer(input)
    stream = CommonTokenStream(lexer)
    parser = StringFigureNotationParser(stream)

    tree = parser.commands()
    walker = ParseTreeWalker()
    listener = MyListener()
    walker.walk(listener, tree)
    for c in listener.commands:
        print(c)
    print('----- normalize ------')
    for c in listener.commands:
        c.normalize()
        print(c)


if __name__ == '__main__':
    main(sys.argv)
