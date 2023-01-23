from enum import IntEnum,auto
from functools import total_ordering


class Finger(IntEnum):
    '''
    指のクラス
    '''
    T=0
    F=1
    M=2
    R=3
    L=4

class Height(IntEnum):
    '''
    ヒモの高さを表す修飾子．
    top と bottom
    '''
    t=10
    b=11

class Depth(IntEnum):
    '''
    ヒモの前後，奥行きを表す修飾子
    近い方(n) と 奥の方(f)
    '''
    n=20
    f=21

class Orientation(IntEnum):
    '''
    ヒモの捻り方
    Move Away と Move Toward
    '''
    MA=30
    MT=31

@total_ordering
class String:
    '''
    ヒモのクラス
    '''
    def __init__(self, height, depth, finger, isString=True):
        self.height = height
        self.depth = depth
        self.finger = finger
        self.isString = isString
        if self.depth == None and self.isString:
            raise ValueError("ヒモS の指定なのに，n,f の指定がありませんでした．:", self)
        elif self.depth != None and not self.isString:
            raise ValueError("ヌーズ N の指定なのに, n,f の指定があります. :", self)

    def __str__(self):
        s = ''
        if self.height != None:
            s += self.height.name
        if self.depth:
            s += self.depth.name
        s += self.finger.name
        if self.isString:
            s += 'S'
        else:
            s += 'N'
        return s

    def __eq__(self, other):
        b = self.height == other.height
        b = b and self.depth == other.depth
        b = b and self.finger == other.finger
        b = b and self.isString == other.isString
        return b

    def __lt__(self, other):
        '''self が other より手前ならTrue, ヌーズならTrue, 上なら True'''
        c = self.finger.value - other.finger.value
        if (c == 0 and self.isString != other.isString):
            if not self.isString:
                c = -1
            else:
                c = 1
        if (c == 0 and self.depth != None and other.depth != None):
            c = self.depth.value - other.depth.value
        if (c == 0):
            c = self.height.value - other.height.value
        return c < 0

@total_ordering
class Move:
    '''
    pickup でヒモの上下を移動することを指定するためのクラス
    mo または mu
    '''
    def __init__(self, isOver, string):
        self.isOver = isOver
        self.string = string

    def __str__(self):
        s = ''
        if self.isOver:
            s += 'mo '
        else:
            s += 'mu '
        return s + str(self.string)

    def __eq__(self, other):
        '''ヒモの等価性 + isOver の等価性'''
        return self.isOver == other.isOver and self.string == other.string

    def __lt__(self, other):
        '''ヒモの大小関係を優先，上を通るならTrue'''
        if self.string == other.string:
            return self.isOver and not other.isOver
        else:
            return self.string < other.string

class Intermediate:
    '''
    アヤトリ表記法の中間表現
    これは抽象クラスで，表記法の構文に従ってサブクラスを持つ
    '''
    def __str__(self):
        return '???'

    def normalize(self):
        '''
        中間表現に必要に応じて変換するメソッド.
        - IPickup: moves の中の move で N があるなら，nS と fS に変換する
            また，指に近い方から取ろうとしているヒモに向かって，moves を並び替える
        - ITwist, IUp, IRe: ヒモが N なら，nS に変更する
        '''
        pass

    def valid(self):
        '''
        中間表現の形式に従っているなら True を返す
        pickup のmove と，up, re のヒモの isString がTrue ならば True を返す
        '''
        return False

class IPickup(Intermediate):
    '''
    pickup の中間表現
    '''
    def __init__(self, finger, moves, string):
        self.finger = finger
        self.moves = moves
        self.string = string

    def __str__(self):
        return self.finger.name + ' ' + ' '.join(map(Move.__str__, self.moves)) + ' pu ' + str(self.string) + ';'

    def valid(self):
        for m in self.moves:
            if not m.string.isString:
                return False
        return True

    def normalize(self):
        moves = []
        # moves の中の N を2つの S に分ける
        for m in self.moves:
            if m.string.isString:
                moves.append(m)
            else:
                s = m.string
                moves.append(Move(m.isOver, String(s.height, Depth.n, s.finger, True)))
                moves.append(Move(m.isOver, String(s.height, Depth.f, s.finger, True)))


        # 指を奥から手前に動かすか？ 手前から奥に動かすか？　を調べる
        f = self.finger
        t = self.string.finger
        if f==t:
            raise ValueError("同じ指のヒモは取れません．")
        isN2F = f.value < t.value   # 手前から奥に動かすなら True

        # moves をソート
        moves.sort(reverse = not isN2F)

        self.moves = moves

class ITwist(Intermediate):
    '''
    twist の中間表現
    '''
    def __init__(self, finger, isAway, string):
        self.finger = finger
        self.isAway = isAway
        self.string = string

    def __str__(self):
        tw = 'ma tw' if self.isAway else 'mt tw'
        return self.finger.name + ' ' + tw + ' ' + str(self.string) + ';'

    def valid(self):
        return self.string.isString

    def normalize(self):
        '''string がヌーズ N なら nS に変更'''
        if not self.string.isString:
            s = self.string
            self.string = String(s.height, Depth.n, s.finger, True)

class IUp(Intermediate):
    '''
    up の中間表現
    '''
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return 'up ' + str(self.string) + ';'

    def valid(self):
        return self.string.isString

    def normalize(self):
        '''string がヌーズ N なら nS に変更'''
        if not self.string.isString:
            s = self.string
            self.string = String(s.height, Depth.n, s.finger, True)

class IRe(Intermediate):
    '''
    re の中間表現
    '''
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return 're ' + str(self.string) + ';'

    def valid(self):
        return self.string.isString

    def normalize(self):
        '''string がヌーズ N なら nS に変更'''
        if not self.string.isString:
            s = self.string
            self.string = String(s.height, Depth.n, s.finger, True)

class IReL(IRe):
    '''
    re-l の中間表現
    '''
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return 're-l ' + str(self.string) + ';'

class IReR(IRe):
    '''
    re-r の中間表現
    '''
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return 're-r ' + str(self.string) + ';'


class IPickupRL(Intermediate):
    '''
    pu-rl の中間表現
    '''
    def __init__(self, finger, string):
        self.finger = finger
        self.string = string

    def __str__(self):
        return self.finger.name + ' pu-rl ' + str(self.string) + ';'

    def valid(self):
        return True

class IPickupLR(Intermediate):
    '''
    pu-lr の中間表現
    '''
    def __init__(self, finger, string):
        self.finger = finger
        self.string = string

    def __str__(self):
        return self.finger.name + ' pu-lr ' + str(self.string) + ';'

    def valid(self):
        return True

class IPickupR(IPickup):
    '''
    pu-r の中間表現
    '''
    def __str__(self):
        return self.finger.name + ' ' + ' '.join(map(Move.__str__, self.moves)) + ' pu-r ' + str(self.string) + ';'

class IPickupL(IPickup):
    '''
    pu-l の中間表現
    '''
    def __str__(self):
        return self.finger.name + ' ' + ' '.join(map(Move.__str__, self.moves)) + ' pu-l ' + str(self.string) + ';'

