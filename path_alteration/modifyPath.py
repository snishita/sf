import sys
import math
from antlr4 import *
from antlr.IntermediateLexer import IntermediateLexer
from antlr.IntermediateParser import IntermediateParser
from antlr.IntermediateListener import IntermediateListener
from antlr.Intermediate import *

### debug option (print verbose information)
#debugMode = True
debugMode = False

# 経路情報.txtの中身を格納
stringRouteNode = []
# ヒモ収縮後の座標値
contractionNode = []
 
# 剛体の座標を格納する
fingerL = []
fingerR = []

#引き伸ばした剛体の座標
extendL = []
extendR = []


# 剛体の半径
rigidBodyRadius = 0.12      # 剛体の半径

### ① 指にかかるヒモを伸ばした後のパラメータ
rdX = 1.15                     # 剛体のX座標
#rdX = 2.15                     # 剛体のX座標
#borderX = 0.95              # 指にかかるヒモと，両手の間のヒモの境目のX座標．ノードのX座標のX座標がこれより大きいとき指にかかるヒモと判定
borderX = rdX-rigidBodyRadius     # 指にかかるヒモと，両手の間のヒモの境目のX座標．ノードのX座標のX座標がこれより大きいとき指にかかるヒモと判定
extendX = 0.3               # 指にかかるヒモの伸ばし幅（X座標）
extendZ = 1.5

### (1.5) 収縮のパラメータ
clusterThreshold = 0.05
#clusterThreshold = 0.15

### ② 収縮後（① の前）のパラメータ
rdContractionX = rdX - extendX*1/2
edgeDistThreshold = 0.01    # 収縮後の線分間の距離の閾値．これより小さいとシミュレーションに失敗する恐れあり
contractionThreshold = 0.9  # 圧縮した時に |ノードのX座標|>この値xborderX のときに圧縮しない
edgeExpandThreshold = 0.02  # 線分の距離がこの閾値よりも小さいときはZ方向にノードを広げる
directionVecZThreshold = 0.6    # 線分の方向ベクトルのZ成分がこの値より小さい時に　〃
expandRateZ = 1.5           # Z方向の拡大倍率
#expandRateZ = 1.0           # Z方向の拡大倍率


### move over/under
detourOverUnder = 0.06


class Node:
    # x,y,z  ノードの座標
    # side  'left'/'right'
    # dhf   ('t'|'b')+('n'|'f')+('T'|'F'|'M'|'R'|'L')
    # dir   contractionNodeのindexの順に見て「両手の中央（x=0）から手指の方向に次のノードが見つかる」とき正の整数, 逆のとき負の整数  
    def __init__(self, x, y, z, side=None, dhf=None, dir=None):
        self.x = x
        self.y = y
        self.z = z
        self.side = side
        self.dhf = dhf
        self.dir = dir
    def clearMark(self):
        self.side = None
        self.dhf = None
        self.dir = None
    def setMark(self, side, dhf, dir):
        self.side = side
        self.dhf = dhf
        self.dir = dir
    def output_str(self, isResult, isHangingNode=False):
        if self.side == None:
            #if isResult or abs(self.x) < borderX:
            if isResult or isHangingNode != True:
                return str((self.x, self.y, self.z+0.05))
            else:
                return str((self.x, self.y, self.z+0.05, "aaa"))
        else:
            return str((self.x, self.y, self.z+0.05, self.side+':'+self.dhf+':'+str(self.dir)))
    def dump(self):
        s = '{x:'+str(self.x)+', y:'+str(self.y)+', z:'+str(self.z)
        if self.side != None:
            s += ', side:'+str(self.side)
        if self.dhf != None:
            s += ', dhf:'+str(self.dhf)
        if self.dir != None:
            s +=', dir:'+str(self.dir)
        s += '}'
        return s

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @staticmethod
    def edge(v1, v2):
        return v2.sub(v1)
    def length(self):
        return math.sqrt(self.length2())
    def length2(self):
        return (self.x*self.x+self.y*self.y+self.z*self.z)
    def sub(self, v):
        return Vec3(self.x-v.x, self.y-v.y, self.z-v.z)
    def innerProd(self, v):
        return self.x*v.x+self.y*v.y+self.z*v.z
    def vectorProd(self, v):
        return Vec3(self.y*v.z-self.z*v.y, self.z*v.x-self.x*v.z, self.x*v.y-self.y*v.x)
    def prod(self, n):
        return Vec3(self.x*n, self.y*n, self.z*n)
    def neighbor(self, v):
        return ((self.x-v.x)**2 + (self.y-v.y)**2 + (self.z-v.z)**2)<clusterThreshold**2
    def norm(self):
        l = self.length()
        return Vec3(self.x/l, self.y/l, self.z/l)
    def __repr__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

class MyListener(IntermediateListener):
    def __init__(self, routeFile):
        self.fingerIndex = {'L':0, 'R':1, 'M':2, 'F':3, 'T':4 }

        # read path file -> stored in stringRouteNode
        self.readFile(routeFile,stringRouteNode)

        # pack path -> the result is stored in contractionNode
        self.allStringContraction(stringRouteNode)

        self.rbStore(fingerL, fingerR)
        self.extendRbStore(extendL,extendR)

        # detect finger nooses and finger strings from the path
        (hangingNodes,wrapped) = self.getHangingNodes(contractionNode, fingerL, fingerR)

        if len(sys.argv) > 3:
            changedRouteFile = open(sys.argv[3], 'w')
            self.outputNodeRoute(contractionNode ,changedRouteFile, False, hangingNodes)


        #self.showContractionNode('after getHangingNodes')

        rgRadius: float = 0.097 # Radius of a rigid body(cylinder) + thickness of the string

        # extend finger strings -> modify contractionNode
        self.extendFingerStrings(rgRadius, contractionNode, hangingNodes, wrapped)

        #self.showContractionNode('after extendFingerString')

        if len(sys.argv) > 4:
            changedRouteFile = open(sys.argv[4], 'w')
            self.outputNodeRoute(contractionNode ,changedRouteFile, False)

    # 指にかかるヒモのノード列を作る
    # 入力: stringRouteNode ファイルから読み込んだ経路情報（ノード列）
    # 出力: ノード列のリスト　　右または左の指にかかるヒモのノード列のリスト（ノード列はノードのリストなので，リストのリストを返す）
    def getHangingNodes(self, stringRouteNode, fingerL, fingerR):
        #print(fingerL)
        #print(rigidBodyRadius)
        #stringRouteNode のインデックスの順に辿って，剛体にかかる紐を構成するノード列を作る
        fingerStringNodeIndices = []
        indices = []
        l = []
        pos = "inside"
        leftBound = fingerL[0][0]
        rightBound = fingerR[0][0]
        prevFinger = None
        self.print('leftBound =', leftBound, '    rightBound =', rightBound)
        finger = self.getFinger(stringRouteNode[3].y, fingerL)
        if stringRouteNode[3].x > leftBound and finger != None:
            pos = "left"
            l.append(3)
        elif stringRouteNode[3].x < rightBound:
            pos = "right"
            l.append(3)
        firstPos = pos
        firstFinger = finger
        for i in range(4,len(stringRouteNode)):
            prevFinger = finger
            finger = self.getFinger(stringRouteNode[i].y, fingerL)  # Y座標がどの指の高さか
            if ((stringRouteNode[i].x > leftBound and pos == "left"
                    or stringRouteNode[i].x < rightBound and pos == "right")
                    and finger == prevFinger):
                # ヒモは依然として指にかかっている
                l.append(i)
            else:
                if l != []:
                    fingerStringNodeIndices.append(l)
                    indices.extend(l)
                    l = []
                if stringRouteNode[i].x > leftBound and finger != None:
                    pos = "left"
                elif stringRouteNode[i].x < rightBound and finger != None:
                    pos = "right"
                else:
                    pos = "inside"
                if pos == 'left' or pos == 'right':
                    l.append(i)
        wrapped = False
        if l != []:
            indices.extend(l)
            # 最後に残った部分を登録する
            if pos == "left" or pos == "right":
                if pos == firstPos and finger == firstFinger:
                    fingerStringNodeIndices[0] = l + fingerStringNodeIndices[0]
                    wrapped = True
                else:
                    fingerStringNodeIndices.append(l)

        # dirty hack
        # leftBound, rightBound の外側で HangingNode でないものを見つける
        # その Node の前後が HangingNode なら，Navaho Extention を考慮して，Nodeのx座標を leftBound, rightBound に変更
        l = indices
        if not(3 in l) and 4 in l and len(stringRouteNode)-1 in l:
            if stringRouteNode[3].x > leftBound:
                stringRouteNode[3].x = leftBound
            elif stringROuteNode[3].x < rightBound:
                stringROuteNode[3].x = rightBound
        for i in range(4, len(stringRouteNode)-1):
            if not(i in l) and (i-1) in l and (i+1) in l:
                if stringRouteNode[i].x > leftBound:
                    stringRouteNode[i].x = leftBound
                elif stringRouteNode[i].x < rightBound:
                    stringRouteNode[i].x = rightBound
        if not(len(stringRouteNode)-1 in l) and 3 in l and len(stringRouteNode)-2 in l:
            if stringRouteNode[len(stringRouteNode)-1].x > leftBound:
                stringRouteNode[len(stringRouteNode)-1].x = leftBound
            elif stringROuteNode[len(stringRouteNode)-1].x < rightBound:
                stringROuteNode[len(stringRouteNode)-1].x = rightBound



        self.print('hangingNodes')
        for l in fingerStringNodeIndices:
            self.print('-----------------------------')
            for i in l:
                self.print(i, stringRouteNode[i].dump())
        

        return (fingerStringNodeIndices, wrapped)

    # 収縮した後のヒモのうち，指にかかる部分だけを左右に広げる
    # 入力: rgRadius 剛体の半径（これより外側を迂回するようにヒモを剛体（指）にかける
    #       contractionNode 収縮後のヒモのノード列
    #       fingerStringNodeIndices 指にかかるヒモのノード列のリスト
    #       wrapped contractionNode の最後の方から始まって，最初の方のノードまでが指にかかったヒモの場合
    # 出力: なし，contractionNode の経路を直接変更する
    def extendFingerStrings(self, rgRadius, contractionNode, fingerStringNodeIndices, wrapped):
        # nearとfarのヒモを格納する辞書
        #   ("nfT"などの文字列) -> [pos,index, dir]
        #       dir: contractionNodeのindexの順に見て「両手の中央（x=0）から手指の方向に次のノードが見つかる」とき正の整数, 逆のとき負の整数
        nfRString = {}
        nfLString = {}

        # 指にかかるヒモを引き伸ばしたヒモに置き換えるため，
        # 引き伸ばしたヒモを作るノードリストを用意する
        newNodes = []
        fingers = ['L', 'R', 'M', 'F', 'T']
        self.print('---------------- extendFingerStrings() ----------------')
        for l in fingerStringNodeIndices:
            isLeft = contractionNode[l[0]].x > 0
            self.print(l[0], contractionNode[l[0]].dump(), isLeft)
            frm = to = -1           # 最初と最後の指
            firstZ = lastZ = 0.0       # 最初と最後のノードのZ座標
            for i in l:
                p = contractionNode[i]
                for j in range(0,5):
                    if abs(p.y - fingerL[j][1]) <= rgRadius:
                        lastZ = p.z
                        to = j
                        if frm == -1:
                            frm = j
                            firstZ = p.z
            isForward = frm<to or frm==to and contractionNode[l[0]].y>contractionNode[l[-1]].y
            rng = range(frm, to+1) if frm<=to else range(frm, to-1, -1)
            self.print('  isForward =', isForward, ', rng =', rng)

            # Z座標の傾きを計算
            dz = (lastZ - firstZ)/(fingerL[to][1]+rgRadius - fingerL[frm][1]+rgRadius)
            
            # 新しいヒモを作成
            newL = []
            baseY = fingerL[frm][1] + (+rgRadius if isForward else -rgRadius)
            f = lambda x,y: Node(x, y, firstZ+dz*(y-baseY))
            for j in rng:
                d = +rgRadius if isForward else -rgRadius
                if isLeft:
                    # left finger

                    # g(k) = (ax, bx, y0, y1)
                    #
                    #                     |
                    # (bx,y1) -------- (ax,y1)     
                    #    |     (剛体) 
                    # (bx,y0) -------- (ax,y0)
                    #                     |
                    #
                    g = lambda k:(+borderX, extendL[k][0]+rgRadius, extendL[k][1]+d, extendL[k][1]-d)
                else:
                    # right finger
                    g = lambda k:(-borderX, extendR[k][0]-rgRadius, extendR[k][1]+d, extendR[k][1]-d)

                (ax, bx, y0, y1) = g(j)
                p0 = f(ax,y0)
                newL.append(p0)
                newL.append(f(bx, y0))
                newL.append(f(bx, y1))
                p1 = f(ax,y1)
                newL.append(p1)

                dpt0 = 'n' if isForward else 'f'
                dpt1 = 'f' if isForward else 'n'

                p0.side = 'left' if isLeft else 'right'
                p1.side = 'left' if isLeft else 'right'
                p0.dir=1
                p1.dir=-1

                p0.dhf = 't'+dpt0+fingers[j]
                p1.dhf = 't'+dpt1+fingers[j]

                # nfLString, nfRString を設定
                mp = nfLString if isLeft else nfRString
                if p0.dhf in mp:
                    dhf0 = 'b'+dpt0+fingers[j]
                    bp0 = mp[p0.dhf]
                    if bp0.z < p0.z:
                        self.print('yes0', p0.dhf, dhf0)
                        #bp0 をbottomに
                        mp[p0.dhf] = p0
                        bp0.dhf = dhf0
                        mp[bp0.dhf] = bp0
                    else:
                        self.print('no0', p0.dhf, dhf0)
                        # p0 をbottomに
                        p0.dhf = dhf0
                        mp[p0.dhf] = p0
                else:
                    mp[p0.dhf] = p0
                if p1.dhf in mp:
                    dhf1 = 'b'+dpt1+fingers[j]
                    bp1 = mp[p1.dhf]
                    if bp1.z < p1.z:
                        self.print('yes1', p1.dhf, dhf1)
                        #bp1 をbottomに
                        mp[p1.dhf] = p1
                        bp1.dhf = dhf1
                        mp[bp1.dhf] = bp1
                    else:
                        self.print('no1', p1.dhf, dhf1)
                        #p1をbottomに
                        p1.dhf = dhf1
                        mp[p1.dhf] = p1
                else:
                    mp[p1.dhf] = p1
                
                '''
                
                if mp.get('t'+dpt0+fingers[j]) != None:
                    r = mp.get('t'+dpt0+fingers[j])
                    if r[0].z < p0.z:
                        # r を bottom に，p0 をtop に
                        mp['b'+dpt0+fingers[j]] = r
                        mp['t'+dpt0+fingers[j]] = [p0, -1, 1]
                    else:
                        # r はtopのまま, p0 をbottom に
                        mp['b'+dpt0+fingers[j]] = [p0, -1, 1]
                else:
                    mp['t'+dpt0+fingers[j]] = [p0, -1, 1]

                if mp.get('t'+dpt1+fingers[j]) != None:
                    r = mp.get('t'+dpt1+fingers[j])
                    if r[0][2] < p1.z:
                        #r をbottom に，p1 をトップに
                        mp['b'+dpt1+fingers[j]] = r
                        mp['t'+dpt1+fingers[j]] = [p1, -1, -1]
                    else:
                        mp['b'+dpt1+fingers[j]] = [p1, -1, -1]
                else:
                    mp['t'+dpt1+fingers[j]] = [p1, -1, -1]
                    '''

            newNodes.append(newL)

        if wrapped:
            # fingerStringNodeIndices[0] のcontractionNode最後の方の点を先に削除しておく
            l = fingerStringNodeIndices[0]
            l.sort(reverse=True)
            last = l[0]+1
            for j,i in enumerate(l):
                if i == last-1:
                    contractionNode.pop(i)
                    last = i
                else:
                    del l[:j]
                    
                    break;
        
        newNodes.reverse()
        for i,l in enumerate(reversed(fingerStringNodeIndices)):
            idx = l[0]
            l.sort(reverse=True)
            for j in l:
                contractionNode.pop(j)
            contractionNode[idx:idx] = newNodes[i]

    def enterCommand(self, ctx:IntermediateParser.CommandContext):
        # ここでリスナーを初期化
        self.fingers = []  # 指はPU の最初，string に出てくるためスタックで管理
        self.finger_side = None
        self.tb = None
        self.nf = None
        self.string = None
        self.string_side = None
        self.moves = [] # 移動は複数回実行する可能性があるので，リストで管理

        self.rbRadius = rigidBodyRadius


    # 剛体の初期座標を格納する
    def rbStore(self, L, R):
        rbPosX = borderX # 元の値　0.9
        rbPosY = 0.9 # 元の値　0.9
        for i in range(5):
            L.append((rbPosX,-rbPosY,0))
            R.append((-rbPosX,-rbPosY,0))
            rbPosY -= 0.45
    # 剛体付近を引き伸ばした時の座標
    def extendRbStore(self, L, R):
        rbPosX = borderX + extendX
        rbPosY = 0.9
        for i in range(5):
            L.append((rbPosX,-rbPosY,0))
            R.append((-rbPosX,-rbPosY,0))
            rbPosY -= 0.45

    # もとの座標において，Y座標からどの指にかかるヒモか推定する
    def getFinger(self, y, lr):
        for f in self.fingerIndex:
            if abs(y-lr[self.fingerIndex[f]][1]) < rigidBodyRadius:
                return f
        return None

    # 文字列の3次元の座標値を分割して返す
    def pointSplit(self, line :str):
        line = line[1:len(line)-1]
        spl = line.split(',')
        x :float= float(spl[0])
        y :float= float(spl[1])
        z :float= float(spl[2])
        return x,y,z

    # 経路情報.txtを読み込み
    def readFile(self, ioFile, inputNode):
        for i,n in enumerate(ioFile):
            n = n.strip()
            # 0~2行目は座標値ではないためスキップ
            if i < 3:
                inputNode.append(n)
                continue
            # 指を表す記号ならスキップ
            if n.startswith('R') or n.startswith('L'):
                continue
            # 座標値をリストとして格納
            vec3 = self.pointSplit(n)
            inputNode.append(vec3)
        del inputNode[-1]       ###################


    # ヒモを収縮する（ノードの位置を横方向で中央寄せする
    # 入力: routeNode 収縮する前のヒモの経路情報
    # 出力: なし, グローバル変数 contractionNode に記録する
    def allStringContraction(self, routeNode: []):
        global contractionNode, rdContractionX, rdX, borderX

        # Y軸の移動量と剛体のX座標を取得
        y_moving = float(routeNode[1])
        rigidX = round(abs(float(routeNode[2])), 3)     # 剛体のX座標
        my = abs(y_moving) + 0.9
        fy = y_moving / my  # Y座標の補正値

        # routeNode の内容を vec3 に変換
        zsum = 0.0;
        vs = []
        for i,_ in enumerate(routeNode):
            if i >= 3:
                v = Vec3(float(routeNode[i][0]), float(routeNode[i][1])+fy, float(routeNode[i][2]))
                vs.append(v)
                zsum += v.z

        zave = 0 if len(routeNode) < 4 else zsum/(len(routeNode)-3)

        #####################################################################
        # X方向の座標を修正（まばらな区間を縮める）
        # 
        # 距離0.15未満の点を1つのクラスタにまとめる
        leftSide = []       # 左手の指に近いノードのクラスタ（v.x < -rigidX+rigidBodyRadius，左と右が逆かも.?）
        rightSide = []      # 右手の指に近いノードのクラスタ（v.x > rigidX-rigidBodyRadius，左と右が逆かも.?）
        cs = []
        for v in vs:
            if v.x < -rigidX+rigidBodyRadius:
                leftSide.append(v)
            elif v.x > rigidX-rigidBodyRadius:
                rightSide.append(v)
            else:
                nearClusters = []
                for cl in cs:
                    done = False
                    for w in cl:
                        if not(done) and v.neighbor(w):
                            nearClusters.append(cl)
                            done = True
                if len(nearClusters) < 1:
                    cs.append([v])
                elif len(nearClusters) == 1:
                    nearClusters[0].append(v)
                else:
                    newcl = []
                    for cl in nearClusters:
                        cs.remove(cl)
                        newcl.extend(cl)
                    newcl.append(v)
                    cs.append(newcl)
        leftSide.sort(key=lambda v:v.x)
        rightSide.sort(key=lambda v:v.x)


        # X軸方向の範囲つきのクラスタを作る
        clusters = []
        for cl in cs:
            minX = maxX = cl[0].x
            for v in cl:
                if v.x < minX:
                    minX = v.x
                if maxX < v.x:
                    maxX = v.x
            clusters.append({"cl":cl, "minX":minX, "maxX":maxX})

        # クラスタをminX が小さい方から順にソート，minXが同じ要素同士は maxXが大きい方を先に
        clusters.sort(key=lambda cl:(cl["minX"], -cl["maxX"]))

        #for cl in clusters:
        #    self.print('min:', cl['minX'], ', max:', cl['maxX'], ', cl:', cl['cl'])

        # X軸方向に圧縮する
        # prevMinX, prevMaxX: 圧縮前のもとのX座標において，x < origX のクラスタは圧縮済み
        #(prevMinX, prevMaxX) = (clusters[0]["minX"], clusters[0]["maxX"])
        (prevMinX, prevMaxX) = (leftSide[-1].x, leftSide[-1].x)
        currentX = prevMinX         # 圧縮前のX座標 prevMinX は圧縮後の currentX 
        gapX = 0                    # 移動量の累積
        singletons = []             # 単一クラスタを見つけたら，ここに格納して，まとめてX軸方向に圧縮する
        minX = currentX
        maxX = currentX
        for c in clusters:
            if prevMaxX < c["minX"]:
                if len(c["cl"]) == 1:
                    #self.print('case1: add to singleton', c)
                    singletons.append(c)
                else:
                    # 単一クラスタの移動
                    #  このX軸方向区間の幅は最大 3*clusterThreshold にする
                    width = min(len(singletons)+1, 3)*clusterThreshold
                    #self.print('case2: width=', width, ', singletons=', singletons, ', c=', c )
                    # [prevMaxX , c["minX"]] の区間を [prevMaxX-gapX, prevMaxX-gapX + width] の区間にマップする
                    a = width / (c["minX"]-prevMaxX)
                    for cc in singletons:
                        v = cc["cl"][0]
                        v.x = prevMaxX-gapX+a*(v.x-prevMaxX)
                        cc["minX"] = cc["maxX"] = v.x

                    # クラスタ c の移動
                    # 移動量の計算
                    #gapX += max(c["minX"] - prevMaxX - clusterThreshold, 0.0)
                    gapX += max(c["minX"] - prevMaxX - width, 0.0)
                    # prevMinX, prevMaxX を更新
                    prevMinX = c["minX"]
                    prevMaxX = c["maxX"]
                    # c.minX, maxX を更新
                    c["minX"] -= gapX
                    c["maxX"] -= gapX
                    # currentX を更新
                    currentX = c["minX"]
                    # 各点を移動
                    for v in c["cl"]:
                        v.x -= gapX
                    #self.print('case2 after: width=', width, ', singletons=', singletons, ', c=', c )
                    singletons = []
            else:
                #self.print('case3: shift', c)
                # 以前のgapX で全ての点を移動
                for v in c["cl"]:
                    v.x -= gapX
                # prevMax を c.maxX にする
                if prevMaxX < c["maxX"]:
                    prevMaxX = c["maxX"]
                c["minX"] -= gapX
                c["maxX"] -= gapX
            if maxX < c["maxX"]:
                maxX = c["maxX"]
        if len(singletons) > 0:
            # 上記の c["minX"] の代わりに rightSide[0].x を使う
            cminX = rightSide[0].x
            width = min(len(singletons)+1, 3)*clusterThreshold
            a = width / (cminX-prevMaxX)
            for c in singletons:
                v = c["cl"][0]
                v.x = prevMaxX-gapX+a*(v.x-prevMaxX)
                c["minX"] = c["maxX"] = v.x
            #self.print('case4: shiftend: width=',width, ', singletons=', singletons)
            singletons = []
            gapX += max(cminX - prevMaxX - width, 0.0)

        # 左手の方は変化なし，右手だけ gapX 分移動
        for v in rightSide:
            v.x -= gapX

        self.print('--------------------------------------')
        #for cl in clusters:
        #    print('min:', cl['minX'], ', max:', cl['maxX'])
        #    self.print('min:', cl['minX'], ', max:', cl['maxX'], ', cl:', cl['cl'])

        # X軸方向の位置補正
        #　gapX が全体の移動量，X座標最小のノードを基準としていた．　したがって，-gapX/2 移動すれば，左右対象になる．
        for c in clusters:
            for v in c["cl"]:
                v.x += gapX/2
            c["minX"] += gapX/2
            c["maxX"] += gapX/2
        for v in leftSide:
            v.x += gapX/2
        for v in rightSide:
            v.x += gapX/2
        
        # 剛体のX座標を補正
        self.print('rigidX: ', rigidX, '  --->  ', rigidX-gapX/2, ',     gapX=', gapX)
        rigidX -= gapX/2
        if rigidX < rdContractionX:
            # rigidX を rdContractionX まで拡大する
            for v in vs:
                v.x = v.x*rdContractionX/rigidX
        else:
            # rigidX はそのまま，rdContractionX などのパラメータを修正
            rdContractionX = rigidX
            rdX = rdContractionX + extendX*1/2
            borderX = rdX-rigidBodyRadius

        #####################################################################
        # Z方向の座標を修正（込み入っている区間を広げる）
        # 少し近い線分を作る点をnvs に記録
        nvs = []
        for i,n1 in enumerate(vs):
            if i < len(vs)-1:
                n2 = vs[i+1]
                last = -2 if i==0 else -1
                for j,n3 in enumerate(vs[i+2:last]):
                    k = j+(i+2)
                    n4 = vs[k+1]
                    (s,d) = self.segmentSegmentDistance3(n1,n2,n3,n4)
                    if d < edgeExpandThreshold and not(j==0 and s == 'point2point'): 
                        v12 = Vec3.edge(n1, n2).norm()
                        v34 = Vec3.edge(n3, n4).norm()
                        if abs(v12.z) < directionVecZThreshold or abs(v34.z) < directionVecZThreshold:
                            nvs.extend([n1, n2, n3, n4])
        '''
        print('----------------------------------------')
        cn = []
        for v in vs:
            if v in nvs:
                cn.append(Node(v.x, v.y, v.z, "bbb", "",""))
            else:
                cn.append(Node(v.x, v.y, v.z))
        f = open('result.txt', 'w')
        self.outputNodeRoute(cn ,f, False)
        '''
        
        # nvs は同じノードが2回以上現れうる．ノードが高々1つだけ含まれるようなリストnsを nvs から作り直す
        ns = []
        for v in vs:
            if v in nvs:
                ns.append(v)
        ns.sort(key=lambda v: v.z)

        # ns からクラスタを構成 閾値は edgeExpandThreshold とする
        cs = []
        for v in ns:
            nearClusters = []
            for cl in cs:
                done = False
                for w in cl:
                    if not(done) and abs(v.z-w.z) < edgeExpandThreshold:
                        nearClusters.append(cl)
                        done = True
            if len(nearClusters) < 1:
                cs.append([v])
            elif len(nearClusters) == 1:
                nearClusters[0].append(v)
            else:
                newcl = []
                for cl in nearClusters:
                    cs.remove(cl)
                    newcl.extend(cl)
                newcl.append(v)
                cs.append(newcl)

        # Z軸方向の範囲つきのクラスタを作る
        clusters = []
        for cl in cs:
            minZ = maxZ = cl[0].z
            for v in cl:
                if v.z < minZ:
                    minZ = v.z
                if maxZ < v.z:
                    maxZ = v.z
            clusters.append({"cl":cl, "minZ":minZ, "maxZ":maxZ, "inside":True})
        clusters.sort(key=lambda c:c["minZ"])

        # clusters に含まれない点も含めたクラスタの集合 cls を作る
        idx = 0             # clusters のインデックス
        inside = False      # クラスタの中か？
        ws = sorted(vs, key=lambda w:w.z)
        cls = []
        if len(clusters) < 1 or ws[0].z < clusters[0]["minZ"]:
            cls.append({"cl":[ws[0]], "minZ": ws[0].z, "maxZ": ws[0].z, "inside":False})
            widx = 1
        else:
            inside = True
            cls.append(clusters[0])
            if ws[0].z <= clusters[0]["maxZ"]:
                widx = 1
                if not(ws[0] in clusters[0]):
                    clusters[0]["cl"].append(ws[0])
                    if ws[0].z < clusters[0]["minZ"]:
                        clusters[0]["minZ"] = ws[0].z
                    elif clusters[0]["maxZ"] < ws[0].z:
                        clusters[0]["maxZ"] = ws[0].z
            else:
                widx = 0
        for v in ws[widx:]:
            while idx < len(clusters) and clusters[idx]["maxZ"] < v.z:
                if cls[-1]!=clusters[idx]:
                    cls.append(clusters[idx])
                idx += 1
            if idx >= len(clusters) or v.z < clusters[idx]["minZ"]:
                if cls[-1]["inside"]:
                    cls.append({"cl":[v], "minZ": v.z, "maxZ": v.z, "inside":False})
                else:
                    if not (v in cls[-1]["cl"]):
                        cls[-1]["cl"].append(v)
                        if v.z < cls[-1]["minZ"]:
                            cls[-1]["minZ"] = v.z
                        elif cls[-1]["maxZ"] < v.z:
                            cls[-1]["maxZ"] = v.z
            else:
                if cls[-1]!=clusters[idx]:
                    cls.append(clusters[idx])
                if not (v in cls[-1]["cl"]):
                    cls[-1]["cl"].append(v)
                    if v.z < cls[-1]["minZ"]:
                        cls[-1]["minZ"] = v.z
                    elif cls[-1]["maxZ"] < v.z:
                        cls[-1]["maxZ"] = v.z
        '''
        print('----------------------------------------')
        for c in sorted(cls, key=lambda c:(c["minZ"], -c["maxZ"])):
            print(c["minZ"], ',', c["maxZ"], '     ', c["inside"])
        cn = []
        for v in vs:
            found = False
            for cl in cls:
                if not(found) and v in cl["cl"] and cl["inside"]:
                    cn.append(Node(v.x, v.y, v.z, str(id(cl)), "",""))
                    found = True
            if not(found):
                cn.append(Node(v.x, v.y, v.z))
        f = open('result.txt', 'w')
        self.outputNodeRoute(cn ,f, False)
        '''

        # Z軸方向に拡張する
        idx = 0             # clusters のインデックス
        offset = 0.0        # 点をZ方向に移動する距離
        offsetGap = 0.0
        for cl in cls:
            if cl["inside"]:
                for v in cl["cl"]:
                    v.z = cl["minZ"]+offset+(v.z-cl["minZ"])*expandRateZ
                offset += (cl["maxZ"]-cl["minZ"])*(expandRateZ-1.0)
            else:
                for v in cl["cl"]:
                    v.z += offset

        # Z座標の調整：0を中心に平行移動
        gapZ = ws[-1].z - ws[0].z
        for v in vs:
            v.z -= gapZ/2




        #####################################################################
        # 線分間の距離をチェック．距離が近すぎる時に警告文を表示
        minD = None
        minSegments = None
        warningFirst = False
        for i,n1 in enumerate(vs):
            if i < len(vs)-1:
                n2 = vs[i+1]
                last = -2 if i==0 else -1
                for j,n3 in enumerate(vs[i+2:last]):
                    k = j+(i+2)
                    n4 = vs[k+1]
                    (s,d) = self.segmentSegmentDistance3(n1,n2,n3,n4)
                    if d < edgeDistThreshold and not(j==0 and s == 'point2point'):
                        if not(warningFirst):
                            self.warning('***********************************************************************')
                            self.warning('X軸方向の収縮により，次の2つの線分の距離が閾値未満で，接近しすぎています')
                            warningFirst = True
                        self.warning((i,i+1),(k,k+1), d)
                        if minD == None or minD > d:
                            minD = d
                            minSegments = (i,i+1,k,k+1)





        # contractionNode の設定
        contractionNode = [0.0, 0.0, rdX]
        for v in vs:
            contractionNode.append(Node(v.x, v.y, v.z))
        return


        # ここまで
        ##############################

        
    # 点p, q の距離が0.15未満ならTrue
    def neighbor(self, p, q):
        return ((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)<0.15**2

    # 剛体の周辺のNodeを取得
    def rgAroundNode(self, node, fingerNodeList: [], rgPos: float, rgRadius: float, index: int):
        if(node[1] >= rgPos - rgRadius and node[1] <= rgPos + rgRadius):
            fingerNodeList.append([node[1],index])
    
    # 剛体周辺のヒモを左右に引き延ばす
    def extendString(self, NodeList: [], rbNodeList: [], LR: str):
        extends = extendX #どの程度ヒモを引き延ばすか調整
        if LR == 'R':
            extends = -extends 
        #for i in range(len(rbNodeList)-1):
        for i,n in enumerate(rbNodeList):
            NodeList[n[1]] = (NodeList[n[1]][0]+extends, NodeList[n[1]][1], NodeList[n[1]][2])
            #NodeList[rbNodeList[i][1]] = (NodeList[rbNodeList[i][1]][0]+extends, NodeList[rbNodeList[i][1]][1], NodeList[rbNodeList[i][1]][2])

    ##########################################################################################
    # 線分の距離を計算するための関数群
    # allStringContraction() の中で，線分同士の距離を計算する必要があるので，その処理をここにまとめる．
    # 参考資料：https://tgws.plus/ul/ul31.html

    def segmentPointDistance(self, n1, n2, n3):
        '''線分n1n2 と 点n3 の距離を計算する'''
        v13 = Vec3.edge(n1,n3)
        v12 = Vec3.edge(n1,n2)
        ip = v13.innerProd(v12)
        if ip < 0:
            return ('point2point', v13.length())
        elif ip < v12.length2():
            return ('point2edge', math.sqrt(v13.length2() - ip*ip/v12.length2()))
        else:
            return ('point2point', Vec3.edge(n2,n3).length())

    def intersected(self, n1, n2, n3, n4):
        '''線分n1n2 と 線分 n3n4 が交差するか判定する．Trueなら交差する． すべての点は同じ平面上にあることを前提とする'''
        v12 = Vec3.edge(n1, n2)
        v34 = Vec3.edge(n3, n4)
        return v12.vectorProd(Vec3.edge(n1, n3)).innerProd(v12.vectorProd(Vec3.edge(n1, n4))) < 0 and v34.vectorProd(Vec3.edge(n3, n1)).innerProd(v34.vectorProd(Vec3.edge(n3, n2))) < 0


    # 使っていない
    def segmentSegmentDistance2(self, n1, n2, n3, n4):
        '''線分n1n2 と 線分 n3n4 の距離を計算する, すべての点は同じ平面上にあることを前提とする'''
        if self.intersected(n1, n2, n3, n4):
            return 0
        else:
            d3 = self.segmentPointDistance(n1, n2, n3)
            d4 = self.segmentPointDistance(n1, n2, n4)
            d1 = self.segmentPointDistance(n3, n4, n1)
            d2 = self.segmentPointDistance(n3, n4, n2)
            return min(d1, d2, d3, d4)

    def segmentSegmentDistance3(self, n1, n2, n3, n4):
        '''線分n1n2 と 線分 n3n4 の距離を計算する, 4点は同じ平面上にあることを前提としない'''
        n = Vec3.edge(n1, n2).vectorProd(Vec3.edge(n3, n4))
        nn31 = n.innerProd(Vec3.edge(n3, n1))
        d = n.prod(nn31/n.length2())
        if self.intersected(n1, n2, n3.sub(d), n4.sub(d)):
            return ('twisted', abs(nn31)/n.length())
        else:
            ps = []
            ps.append(self.segmentPointDistance(n1, n2, n3))
            ps.append(self.segmentPointDistance(n1, n2, n4))
            ps.append(self.segmentPointDistance(n3, n4, n1))
            ps.append(self.segmentPointDistance(n3, n4, n2))
            (s, d) = ps[0]
            for (ss,dd) in ps[1:]:
                if dd < d:
                    (s, d) = (ss, dd)
            return (ss, dd)
            


    # ここまで：線分の距離を計算する関数群
    #####################################
        

    def exitFinger(self, ctx:IntermediateParser.FingerContext):
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

    def exitTb(self, ctx:IntermediateParser.TbContext):
        if ctx.HT():
            self.tb = Height.t
        elif ctx.HB():
            self.tb = Height.b
        else:
            self.tb = None
    def exitNf(self, ctx:IntermediateParser.NfContext):
        self.print("ctx.DN():", ctx.DN(), ", ctx.DF():", ctx.DF());
        if ctx.DN():
            self.nf = Depth.n
        elif ctx.DF():
            self.nf = Depth.f
        else:
            #self.nf = Depth.f
            self.nf = None

    def exitString(self, ctx:IntermediateParser.StringContext):
        self.print("tb:", self.tb, ", nf:", self.nf, "fingers:", self.fingers)
        self.string = String(self.tb, self.nf, self.fingers.pop(), True if ctx.S() else False)
        self.tb = self.nf = None
        # self.fingers はpop() によって削除済み

    def exitMove(self, ctx:IntermediateParser.MoveContext):
        self.moves.append(Move(True if ctx.MO() else False, self.string))
        self.string = None

    def exitCommand(self, ctx:IntermediateParser.CommandContext):
        if ctx.UP():
            #self.showContractionNode('before UP')
            (height, depth, finger, target) = self.getString()

            if target == 'N':
                depth = 'n'     # この後の外す処理では，nf どちらでも同じ結果になる

            string = height + depth + finger
            self.upNodeNew(string)
            #self.showContractionNode('after UP')

        
        elif ctx.RE():
            self.printNfLRString(True, 'before re')
            (height, depth, finger, target) = self.getString()

            if target == 'N':
                depth = 'n'     # この後の外す処理では，nf どちらでも同じ結果になる
            
            string = height + depth + finger
            
            if height == 'b':
                self.upNodeNew(string);
                height = 't'
                string = 't'+depth+finger
                self.printNfLRString(True, 'before re but after up')
            
            otherSideString = height + ('n' if depth=='f' else 'f') + finger
            
            tasks = []
            # idx が後ろの側のヒモからはずす
            (sli,sln) = self.findNode("left", string)
            (sri,srn) = self.findNode("right", string)
            (oli,oln) = self.findNode("left", otherSideString)
            (ori,orn) = self.findNode("right", otherSideString)
            if sli > sri:
                tasks = [(sli, oli), (sri, ori)]
            else:
                tasks = [(sri, ori), (sli, oli)]
            for (frm,to) in tasks:
                if frm>to:
                    frm,to = to,frm
                self.reNoose(frm, to)
            sln.clearMark()
            srn.clearMark()
            oln.clearMark()
            orn.clearMark()

            bottomString = 'b' + depth + finger
            bottomOtherSideString = 'b' + ('n' if depth=='f' else 'f') + finger
            slp = self.findNode("left", bottomString)
            srp = self.findNode("right", bottomString)
            olp = self.findNode("left", bottomOtherSideString)
            orp = self.findNode("right", bottomOtherSideString)
            if slp != None:
                slp[1].dhf = string
            if srp != None:
                srp[1].dhf = string
            if olp != None:
                olp[1].dhf = otherSideString
            if orp != None:
                orp[1].dhf = otherSideString

            self.printNfLRString(True, 'after re')

        elif ctx.REL():
            print('REL is not implemented yet')
        elif ctx.RER():
            print('RER is not implemented yet')
        elif ctx.TW():
            finger = self.fingers.pop().name
            isMA = True if ctx.MA() else False  # maならtrue,mtならfalse

            (height, depth, fingerString, target) = self.getString()

            if target == 'S' :
                raise ValueError("twist ではヒモ S を指定できません．代わりにヒモの輪 Nを指定してください", self)
            if height == 'b' : 
                raise ValueError("twist では一番上のヒモだけを取ることができます．下のヒモ b を指定しないでください", self)
            if fingerString != finger :
                raise ValueError("twist では，指にかかるヒモが指と同じでなくてはいけません．", self)

            # 指，捻り方，ヒモの内容を取得して，ヒモを捻るように経路情報を変更
            (lnidx, _) = self.findNode("left", 'tn'+finger)
            (rnidx, _) = self.findNode("right", 'tn'+finger)
            if rnidx < lnidx:
                self.twistNoose(isMA, True, finger)     # True... 左を意味する
                self.twistNoose(isMA, False, finger)     # False... 右を意味する
            else:
                self.twistNoose(isMA, False, finger)     # False... 右を意味する
                self.twistNoose(isMA, True, finger)     # True... 左を意味する

        elif ctx.PURL():
            print('PURL is not implemented yet')

        elif ctx.PULR():
            print('PULR is not implemented yet')
        elif ctx.PUR():
            print('PULR is not implemented yet')
        elif ctx.PUL():
            print('PULR is not implemented yet')
        else:   # ctx.PU()
            finger = self.fingers.pop().name
            moves = self.moves
            (height, depth, fingerString, target) = self.getString()
            if target == 'S':
                # ヒモを取る
                # 指，上下の移動列，ヒモの内容を取得して，左右指で左右同じ側のヒモを取るように経路情報を変更
                string = height+depth+fingerString
                (lnidx, _) = self.findNode('left', string)
                (rnidx, _) = self.findNode('right', string)
                if lnidx < rnidx:
                    self.rightPu(finger,moves,string)
                    self.leftPu(finger,moves,string)
                else:
                    self.leftPu(finger,moves,string)
                    self.rightPu(finger,moves,string)
            else:
                # Noose（ワッカ）を別の指に移動
                # move は空リストである前提（途中の紐の下を通ってというのは現実において不自然）
                if len(moves) > 0:
                    raise ValueError("Noose を取る場合には mo, mu は指定できません．（途中の紐の上を通って，Noose を移動させます）", self)
                
                if depth==None:
                    depth = 'n'
                string = height + depth + fingerString
                
                # 下のヒモを移動する場合は，事前に UP が必要
                if height == 'b':
                    self.upNodeNew(string)
                    height = 't'
                    string = 't'+depth+fingerString

                self.printNfLRString(title='before pu Noose')
                
                # Noose の移動
                (lnidx, _) = self.findNode('left', string)
                (rnidx, _) = self.findNode('right', string)
                if lnidx < rnidx:
                    self.rightPuNoose(finger, fingerString)
                    self.leftPuNoose(finger, fingerString)
                else:
                    self.leftPuNoose(finger, fingerString)
                    self.rightPuNoose(finger, fingerString)
                self.printNfLRString(title='after pu Noose')



    # string を上にあげる．string は 'b' で始まる3文字で，このヒモの上には同じ指にかかる別のヒモがある前提
    def upNodeNew(self, string):
        height,depth,finger = string

        otherSideString = height + ('n' if depth=='f' else 'f') + finger
        aboveString = 't' + depth+finger
        aboveOtherSideString = 't' + ('n' if depth=='f' else 'f') + finger

        ln = self.findNode('left', string)
        rn = self.findNode('right', string)
        lo = self.findNode('left', otherSideString)
        ro = self.findNode('right', otherSideString)
        la = self.findNode('left', aboveString)
        ra = self.findNode('right', aboveString)
        lao = self.findNode('left', aboveOtherSideString)
        rao = self.findNode('right', aboveOtherSideString)
        
        if ln == None or rn == None :
            print('エラー: 上方に引きあげるヒモが見つかりません')
            print("string:", string)
            self.printNfLRString()
            return
        if lo == None or ro == None:
            print('エラー: 上方に引きあげるヒモの指定されたノードの反対側のノードが見つかりません')
            print("otherSideString:", otherSideString)
            self.printNfLRString()
            return
        if la == None or ra == None:
            print('エラー: 引きあげたいヒモの上にあるはずのヒモが見つかりません')
            print("aboveString:", aboveString)
            self.printNfLRString()
            return
        if lao == None or rao == None:
            print('エラー: 引きあげたいヒモの上の反対側のヒモが見つかりません')
            print("aboveOtherSideString:", aboveOtherSideString)
            self.printNfLRString()
            return

        # 左右を繰り返し処理
        #  index が後の方から先に処理
        #  上方のヒモのindex が壊れる可能性があるので，
        #  nfLString/nfRString から先に必要な情報を取り出しておいて，その後経路を変更する
        tuples = []
        if ln[0] > rn[0]:
            tuples.append((ln[1], ln[0], lo[0], la[1]))
            tuples.append((rn[1], rn[0], ro[0], ra[1]))
        else:
            tuples.append((rn[1], rn[0], ro[0], ra[1]))
            tuples.append((ln[1], ln[0], lo[0], la[1]))
        # tuples に必要な情報を格納完了．tuples の情報を使って経路変更
        for (stringPos, stringIdx, otherSideStringIdx, aboveStringPos) in tuples :
            dz = aboveStringPos.z + 0.1 - stringPos.z
            frmIdx, toIdx = (stringIdx, otherSideStringIdx) if stringIdx<otherSideStringIdx else (otherSideStringIdx, stringIdx)
            dist = 0.04         # 迂回路の幅(X,Y方向それぞれ)
            detourX = dist if stringPos.x > 0 else (-dist)
            detourY = dist if stringIdx<otherSideStringIdx and depth=='n' or stringIdx>otherSideStringIdx and depth=='f' else (-dist)
            self.upNoose(frmIdx, toIdx, dz, detourX, detourY)

        # u <-> b のヒモの記録を入れ替える
        ln[1].dhf = aboveString
        la[1].dhf = string
        lo[1].dhf = aboveOtherSideString
        lao[1].dhf = otherSideString
        rn[1].dhf = aboveString
        ra[1].dhf = string
        ro[1].dhf = aboveOtherSideString
        rao[1].dhf = otherSideString

    # 左側のみpu
    def leftPu(self, finger: str, moves: [], string: str):
        fingerIndex = self.fingerIndex
        
        (index, node) = self.findNode('left', string)
        index = index + (1 if node.dir < 0 else 0)

        puFinger = extendL[fingerIndex[finger]]
        rbRadius = self.rbRadius
        nz = node.z
        # 指に既にヒモが掛かっている場合、そのヒモからz+n上にヒモ掛ける

        ffs = 'tf'+finger
        nfs = 'tn'+finger
        
        tn = self.findNode('left', nfs)
        if tn != None:
            nz = tn[1].z
            tn[1].dhf = 'bn'+finger
        tf = self.findNode('left', ffs)
        if tf != None:
            nz = tf[1].z if tf[1].z > nz else nz
            tf[1].dhf = 'bf'+finger
        
        # 取る指より取るヒモが奥の場合
        if fingerIndex[finger] > fingerIndex[string[-1]]:
            if node.dir > 0: 
                self.print('aaa+')
                index += 1
                # contractionNode[index] → contractionNode[index+1] のヒモの間に追加
                # 取るヒモから取る指に向かってmo/muするため、movesを逆順に
                contractionNode.insert(index, Node(node.x+0.1,node.y,node.z, 'left', node.dhf, node.dir))
                self.overUnder(contractionNode, index, reversed(moves), -1, 'left', 0.2)
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'left', ffs, -node.dir))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'left', nfs, node.dir))
                self.overUnder(contractionNode, index, moves, 1, 'left', 0.1)
            else:
                self.print('aaa-')
                index -= 1
                # contractionNode[index-1] → contractionNode[index] のヒモの間に追加
                # 取るヒモから取る指に向かってmo/muするため、movesを逆順に
                self.overUnder(contractionNode, index, reversed(moves), -1, 'left', 0.1)
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'left', nfs, node.dir))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'left', ffs, -node.dir))
                self.overUnder(contractionNode, index, moves, 1, 'left', 0.2)
                contractionNode.insert(index, Node(node.x+0.1,node.y,node.z, 'left', node.dhf, node.dir))

        # 取る指より取るヒモが手前の場合
        elif fingerIndex[finger] < fingerIndex[string[-1]]:
            if node.dir > 0:
                self.print('bbb+')
                index += 1
                contractionNode.insert(index, Node(node.x+0.1,node.y,node.z, 'left', node.dhf, node.dir))
                self.overUnder(contractionNode, index, reversed(moves), 1, 'left', 0.2)
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'left', nfs, -node.dir))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'left', ffs, node.dir))
                self.overUnder(contractionNode, index, moves, -1, 'left', 0.1)
            else :
                self.print('bbb-')
                index -= 1
                self.overUnder(contractionNode, index, reversed(moves), 1, 'left', 0.1)
                #contractionNode.insert(index, (puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'b'))
                #contractionNode.insert(index, (puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'd'))
                #contractionNode.insert(index, (puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'c'))
                #contractionNode.insert(index, (puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'a'))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'left', ffs, node.dir))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'left', nfs, -node.dir))
                self.overUnder(contractionNode, index, moves, -1, 'left', 0.2)
                #contractionNode.insert(index, (x+0.1,y,z, 'e'))
                contractionNode.insert(index, Node(node.x+0.1,node.y,node.z, 'left', node.dhf, node.dir))
        node.clearMark()

    # 右側のみpu
    def rightPu(self, finger: str, moves: [], string: str):
        fingerIndex = self.fingerIndex
        (index, node) = self.findNode('right', string)
        index = index + (1 if node.dir < 0 else 0)
        puFinger = extendR[fingerIndex[finger]]
        rbRadius = self.rbRadius
        nz = node.z
        nfs = 'tn'+finger
        ffs = 'tf'+finger
        tn = self.findNode('right', nfs)
        if tn != None:
            nz = tn[1].z
            tn[1].dhf = 'bn'+finger
        tf = self.findNode('right', ffs)
        if tf != None:
            nz = tf[1].z if tf[1].z > nz else nz
            tf[1].dhf = 'bf'+finger
        # 取る指より取るヒモが奥の場合
        if fingerIndex[finger] > fingerIndex[string[-1]]:
            if node.dir > 0:
                self.print('ccc+')
                index += 1
                contractionNode.insert(index, Node(node.x-0.1,node.y,node.z, 'right', node.dhf, node.dir))
                self.overUnder(contractionNode, index, reversed(moves), -1, 'right', -0.2)
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'right', ffs, -node.dir))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'right', nfs, node.dir))
                self.overUnder(contractionNode, index, moves, 1, 'right', -0.1)
            else:
                self.print('ccc-')
                index -= 1
                self.overUnder(contractionNode, index, reversed(moves), -1, 'right', -0.1)
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'right', nfs, node.dir))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'right', ffs, -node.dir))
                self.overUnder(contractionNode, index, moves, 1, 'right', -0.2)
                contractionNode.insert(index, Node(node.x-0.1,node.y,node.z, 'right', node.dhf, node.dir))

        # 取る指より取るヒモが手前の場合
        elif fingerIndex[finger] < fingerIndex[string[-1]]:
            if node.dir > 0:
                self.print('ddd+')
                index += 1
                contractionNode.insert(index, Node(node.x-0.1,node.y,node.z, 'right', node.dhf, node.dir))
                self.overUnder(contractionNode, index, reversed(moves), 1, 'right', -0.2)
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'right', nfs, -node.dir))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'right', ffs, node.dir))
                self.overUnder(contractionNode, index, moves, -1, 'right', -0.1)
            else:
                self.print('ddd-')
                index -= 1
                self.overUnder(contractionNode, index, reversed(moves), 1, 'right', -0.1)
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]-rbRadius,nz + 0.2, 'right', ffs, node.dir))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]-rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]-rbRadius,puFinger[1]+rbRadius,nz + 0.2))
                contractionNode.insert(index, Node(puFinger[0]+rbRadius,puFinger[1]+rbRadius,nz + 0.2, 'right', nfs, -node.dir))
                self.overUnder(contractionNode, index, moves, -1, 'right', -0.2)
                contractionNode.insert(index, Node(node.x-0.1,node.y,node.z, 'right', node.dhf, node.dir))
        node.clearMark()

    def leftPuNoose(self, finger: str, fingerString: str):
        fingerIndex = self.fingerIndex

        # finger - fingerString の指にかかるヒモのすべての高さの最大 maxzを求める
        fingers = ['L', 'R', 'M', 'F', 'T']
        heightdepth = ['tn', 'tf']
        inRange = False
        maxz = -10
        for f in fingers:
            prevInRange = inRange
            if f == finger or f == fingerString:
                inRange = not(inRange)
            for hd in heightdepth:
                s = hd+f
                sn = self.findNode('left', s)
                if (inRange or prevInRange) and sn!=None:
                    z = sn[1].z
                    maxz = maxz if maxz >= z else z
                if not(inRange) and prevInRange:
                    break
            inRange = prevInRange
        
        # 追加するヒモの経路の高さ newh を maxz+.2 に設定

        newh = maxz + 0.2

        puFinger = extendL[fingerIndex[finger]]
        rbRadius = self.rbRadius

        nString, fString = ('tn'+fingerString, 'tf'+fingerString)
        (fx, fy, _) = extendL[fingerIndex[finger]]
        (idxn, nn) = self.findNode('left', nString)
        (idxf, nf) = self.findNode('left', fString)

        nfs, ffs = ('tn'+finger, 'tf'+finger)
        (pn, pf) = (self.findNode('left', nfs), self.findNode('left', ffs))
        if pn != None:
            pn[1].dhf = 'bn'+finger
        if pf != None:
            pf[1].dhf = 'bf'+finger

        # 4つに場合わけ
        if nn.dir > 0:
            del contractionNode[idxn+1:idxf]
            # 1. nString のインデックス < fString のインデックス
            if fingerIndex[finger] > fingerIndex[fingerString]:
                self.print('対象1.1')
                # 1.1 fingerIndex[finger] > fingerIndex[fingerString]
                #   (nf.x, nf.y, nf.z)既存 <- (nf.x, nf.y, newh)
                #                       <- (nf.x+0.05, nf.y, newh)
                #                       <- (nf.x+0.05, fy-rbRadius, newh)
                #                       <- (fx+rbRadius, fy-rbRadius, newh)
                #                       <- (fx+rbRadius, fy+rbRadius, newh)
                #                       <- (fx-rbRadius, fy+rbRadius, newh)
                #                       <- (nn.x, fy+rbRadius, newh)
                #                       <- (nn.x, nn.y, newh)
                #                       <- (nn.x, nn.y, nn.z) 既存
                # 途中，既存の点はすべて使う（新しい点を作るのではなく，既存の点の座標を変更する）
                idxn += 1
                contractionNode.insert(idxn, Node(nf.x+0.05, nf.y, newh))
                contractionNode.insert(idxn, Node(nf.x+0.05, fy-rbRadius, newh, 'left', ffs, nf.dir))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy+rbRadius, newh, 'left', nfs, nn.dir))
                contractionNode.insert(idxn, Node(nn.x, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(nn.x, nn.y, newh))
            else:
                self.print('対象1.2')
                idxn += 1
                contractionNode.insert(idxn, Node(nf.x, nf.y, newh))
                contractionNode.insert(idxn, Node(nf.x, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy-rbRadius, newh, 'left', ffs, nf.dir))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(nn.x+0.05, fy+rbRadius, newh, 'left', nfs, nn.dir))
                contractionNode.insert(idxn, Node(nn.x+0.05, nn.y, newh))
        else:
            del contractionNode[idxf+1:idxn]
            # 2. nString のインデックス > fString のインデックス
            if fingerIndex[finger] > fingerIndex[fingerString]:
                self.print('対象2.1')
                idxf += 1
                contractionNode.insert(idxf, Node(nn.x, nn.y, newh))
                contractionNode.insert(idxf, Node(nn.x, fy+rbRadius, newh))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy+rbRadius, newh, 'left', nfs, nn.dir))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(nf.x+0.05, fy-rbRadius, newh, 'left', ffs, nf.dir))
                contractionNode.insert(idxf, Node(nf.x+0.05, nf.y, newh))
            else:
                self.print('対象2.2')
                idxf += 1
                contractionNode.insert(idxf, Node(nn.x+0.05, nn.y, newh))
                contractionNode.insert(idxf, Node(nn.x+0.05, fy+rbRadius, newh, 'left', nfs, nn.dir))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy-rbRadius, newh, 'left', ffs, nf.dir))
                contractionNode.insert(idxf, Node(nf.x, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(nf.x, nf.y, newh))
        nn.clearMark()
        nf.clearMark()

    def rightPuNoose(self, finger: str, fingerString: str):
        self.print(finger[-1], fingerString)
        fingerIndex = self.fingerIndex

        # finger - fingerString の指にかかるヒモのすべての高さの最大 maxzを求める
        fingers = ['L', 'R', 'M', 'F', 'T']
        heightdepth = ['tn', 'tf']
        inRange = False
        maxz = -10
        for f in fingers:
            prevInRange = inRange
            if f == finger[-1] or f == fingerString:
                inRange = not(inRange)
            for hd in heightdepth:
                s = hd+f
                sn = self.findNode('right', s)
                if (inRange or prevInRange) and sn != None:
                    z = sn[1].z
                    maxz = maxz if maxz >= z else z
                if not(inRange) and prevInRange:
                    break
            inRange = prevInRange
        
        # 追加するヒモの経路の高さ newh を maxz+.2 に設定

        newh = maxz + 0.2

        puFinger = extendR[fingerIndex[finger[-1]]]
        rbRadius = self.rbRadius

        nString, fString = ('tn'+fingerString, 'tf'+fingerString)
        (fx, fy, _) = extendR[fingerIndex[finger[-1]]]
        (idxn, nn) = self.findNode('right', nString)
        (idxf, nf) = self.findNode('right', fString)

        nfs, ffs = ('tn'+finger, 'tf'+finger)
        (pn, pf) = (self.findNode('right', nfs), self.findNode('right', ffs))
        if pn != None:
            pn[1].dhf = 'bn'+finger
        if pf != None:
            pf[1].dhf = 'bf'+finger


        # 4つに場合わけ
        if nn.dir > 0:
            del contractionNode[idxn+1:idxf]
            # 1. nString のインデックス < fString のインデックス
            if fingerIndex[finger[-1]] > fingerIndex[fingerString]:
                self.print('R対象1.1')
                # 1.1 fingerIndex[finger] > fingerIndex[fingerString]
                #   (nf.x, nf.y, nf.z)既存 <- (nf.x, nf.y, newh)
                #                       <- (nf.x+0.05, nf.y, newh)
                #                       <- (nf.x+0.05, fy-rbRadius, newh)
                #                       <- (fx+rbRadius, fy-rbRadius, newh)
                #                       <- (fx+rbRadius, fy+rbRadius, newh)
                #                       <- (fx-rbRadius, fy+rbRadius, newh)
                #                       <- (nn.x, fy+rbRadius, newh)
                #                       <- (nn.x, nn.y, newh)
                #                       <- (nn.x, nn.y, nn.z) 既存
                # 途中，既存の点はすべて使う（新しい点を作るのではなく，既存の点の座標を変更する）
                idxn += 1
                contractionNode.insert(idxn, Node(nf.x-0.05, nf.y, newh))
                contractionNode.insert(idxn, Node(nf.x-0.05, fy-rbRadius, newh, 'right', ffs, nf.dir))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy+rbRadius, newh, 'right', nfs, nn.dir))
                contractionNode.insert(idxn, Node(nn.x, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(nn.x, nn.y, newh))
            else:
                self.print('R対象1.2')
                idxn += 1
                contractionNode.insert(idxn, Node(nf.x, nf.y, newh))
                contractionNode.insert(idxn, Node(nf.x, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx+rbRadius, fy-rbRadius, newh, 'right', ffs, nf.dir))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxn, Node(fx-rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxn, Node(nn.x-0.05, fy+rbRadius, newh, 'right', nfs, nn.dir))
                contractionNode.insert(idxn, Node(nn.x-0.05, nn.y, newh))
        else:
            del contractionNode[idxf+1:idxn]
            # 2. nString のインデックス > fString のインデックス
            if fingerIndex[finger[-1]] > fingerIndex[fingerString]:
                self.print('R対象2.1')
                idxf += 1
                contractionNode.insert(idxf, Node(nn.x, nn.y, newh))
                contractionNode.insert(idxf, Node(nn.x, fy+rbRadius, newh))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy+rbRadius, newh, 'right', nfs, nn.dir))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(nf.x-0.05, fy-rbRadius, newh, 'right', ffs, nf.dir))
                contractionNode.insert(idxf, Node(nf.x-0.05, nf.y, newh))
            else:
                self.print('R対象2.2')
                idxf += 1
                contractionNode.insert(idxf, Node(nn.x-0.05, nn.y, newh))
                contractionNode.insert(idxf, Node(nn.x-0.05, fy+rbRadius, newh, 'right', nfs, nn.dir))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy+rbRadius, newh))
                contractionNode.insert(idxf, Node(fx-rbRadius, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(fx+rbRadius, fy-rbRadius, newh, 'right', ffs, nf.dir))
                contractionNode.insert(idxf, Node(nf.x, fy-rbRadius, newh))
                contractionNode.insert(idxf, Node(nf.x, nf.y, newh))
        nn.clearMark()
        nf.clearMark()

    def reNoose(self, frmIdx: int, toIdx: int):
        # contractionNode[frmIdx+1] 〜 contractionNode[toIdx-1] を削除する
        self.print('#######################################################################')
        self.print('reNoose(', frmIdx, ', ', toIdx, ')     before..')
        self.printNfLRString(False)
        del contractionNode[frmIdx+1:toIdx]
        self.print('reNoose(', frmIdx, ', ', toIdx, ')     after..')
        self.printNfLRString(False)
    
    def upNoose(self, frmIdx: str, toIdx: str, dz: float, detourX: float, detourY: float):
        # contractionNode[frmIdx] 〜 controctionNode[toIdx] の点で構成されるヒモを dz だけ上に引きあげる処理
        # frmIdx < toIdx であり，この向きに点がつながっていることを前提とする
        # また，引きあげるヒモの 上方に同じ指にかかるヒモがあることを想定する．このヒモを迂回するように引きあげる必要がある
        # (detourX, detourY) はfrmIdx のノードにおいて迂回させる距離と向きを意味する
        # toIdx のノードにおいては，(detourX, -detourY) の向きに迂回させる
        # 戻り値として，contractionNode[frmIdx] と contractionNode[toIdx] それぞれから dz だけ上方に新しく作ったノードのタプルを返す
        #
        # やり方：contractionNode[frmIdx]と contractionNode[toIdx] は指につながるヒモと両手の間の中央部分の境目のノードである
        #         ノードの x 座標は ±0.95 のはず（参照; extendFingerStrings() の関数g
        #         x=±0.95 の平面において，迂回路を作る．この平面での断面の様子を以下の図に示す．
        #         （20210319 修正) x=±0.95 の平面だと，迂回したヒモが別のヒモと重なることがあるため，上からみて斜め，x±y=n 方向に迂回させる
        #                          このため，detourX,detourY の2つのパラメータを使って迂回させることにした
        # 
        # ~~~~~~~~~~~~~~~~~~~~~~~~
        #
        #  z
        #  ↑       
        #          +----+   ..........
        #               |       ↑
        #          x    |      dz
        #               |       ↓
        #  →y      o----+   ..........
        #          :    :
        #         →:    :← detourX/detourY
        #
        #  o: contractionNode[frmIdx]
        #  x: 迂回させるヒモの x=±0.95 における境界点
        #  +: 追加する点
        #  contractionNode[frmIdx+1] から先のノードは，dz 分上方に移動させる
        # 

        ##### debug
        #print('#######################################################################')
        #print('upNoose(', frmIdx, ', ', toIdx, ', ', dz, ', ', detourX, ', ', detourY, ')     before..')
        #self.printNfLRString()
        
        # contractionNode[frmIdx+1] 〜 contractionNode[toIdx-1] のZ座標を変更（上方に引きあげる）
        for i in range(frmIdx+1, toIdx):
            contractionNode[i].z += dz
        
        # contractionNode[toIdx+1] に迂回路を追加
        # contractionNode[toIdx] は情報に移動する（このノードが，指にかかるヒモとして登録されている）
        p = contractionNode[toIdx]
        contractionNode.insert(toIdx+1, Node(p.x, p.y, p.z))    # p と同じに配置．pはこの後上方に移動する
        contractionNode.insert(toIdx+1, Node(p.x+detourX, p.y-detourY, p.z))
        contractionNode.insert(toIdx+1, Node(p.x+detourX, p.y-detourY, p.z+dz))
        p.z += dz   # p を上方に移動
        
        # contractionNode[frmIdx] に迂回路を追加
        p = contractionNode[frmIdx]
        contractionNode.insert(frmIdx, Node(p.x+detourX, p.y+detourY, p.z+dz))
        contractionNode.insert(frmIdx, Node(p.x+detourX, p.y+detourY, p.z))
        contractionNode.insert(frmIdx, Node(p.x, p.y, p.z))
        p.z += dz


    # string を取り出す
    def getString(self):
        string = str(self.string)
        target = string[-1]     # S, T のいずれか

        finger = string[-2]

        s = string[:-2]
        idx = 0
        if len(s) > idx and (s[idx] == 't' or s[idx] == 'b'):
            height = s[idx]
            idx += 1
        else:
            height = 't'
        
        if len(s) > idx:
            if s[idx] == 'n' or s[idx] == 'f':
                depth = s[idx]
            else:
                raise ValueError("ヒモの指定 "+string+" が無効です．この文字列の "+str(idx)+" 番目には depth を指定するはずですが，別の文字が指定されています")
        else:
            depth = None
        if target == 'S' and depth == None:
            raise ValueError("ヒモの指定 "+string+" が無効です．'S'を指定する場合は，depth として 'n' または 'f' を合わせて指定してください")
        return (height, depth, finger, target)

    def getOtherSide(self, dhf):
        height, depth, finger = dhf
        return (height+ ('n' if depth=='f' else 'f') + finger)

    def twistNoose(self, isMa, isLeft, finger):
        if isLeft:
            (fx, fy, _) = extendL[self.fingerIndex[finger]]
        else:
            (fx, fy, _) = extendR[self.fingerIndex[finger]]
        rbRadius = self.rbRadius
        twstep = 0.025 if isLeft else -0.025
        xoffset = rbRadius if isLeft else -rbRadius

        zoffset = 0.1 if isMa else -0.1
        
        side = 'left' if isLeft else 'right'
        s0 = 'tn'+finger
        s1 = 'tf'+finger
        idx0, n0 = self.findNode(side, s0)
        idx1, n1 = self.findNode(side, s1)
        if idx0 < idx1:
            yoffset = rbRadius
        else:
            idx0, idx1 = idx1, idx0
            s0, s1 = s1, s0
            n0, n1 = n1, n0
            yoffset = -rbRadius
            zoffset = -zoffset

        self.print('isMa =', isMa, ', isLeft =', isLeft, ', finger =', finger)
        self.print('twstep =', twstep, ', xoffset =', xoffset)
        self.print('yoffset =', yoffset, ', zoffset =', zoffset)

        del contractionNode[idx0+1:idx1]
        idx = idx0+1
        z = (n0.z+n1.z)/2.0
        contractionNode.insert(idx, Node(n1.x+twstep, n1.y, n1.z))
        contractionNode.insert(idx, Node(n1.x+twstep, fy-yoffset, z))
        contractionNode.insert(idx, Node(n1.x+2*twstep, fy, z-zoffset))
        contractionNode.insert(idx, Node(n1.x+3*twstep, fy+yoffset, z))
        contractionNode.insert(idx, Node(n1.x+4*twstep, fy, z+zoffset))
        contractionNode.insert(idx, Node(n1.x+5*twstep, fy-yoffset, z))
        contractionNode.insert(idx, Node(fx-xoffset, fy-yoffset, z))
        contractionNode.insert(idx, Node(fx+xoffset, fy-yoffset, z))
        contractionNode.insert(idx, Node(fx+xoffset, fy+yoffset, z))
        contractionNode.insert(idx, Node(fx-xoffset, fy+yoffset, z))
        contractionNode.insert(idx, Node(n0.x+5*twstep, fy+yoffset, z))
        contractionNode.insert(idx, Node(n0.x+4*twstep, fy, z-zoffset))
        contractionNode.insert(idx, Node(n0.x+3*twstep, fy-yoffset, z))
        contractionNode.insert(idx, Node(n0.x+2*twstep, fy, z+zoffset))
        contractionNode.insert(idx, Node(n0.x+twstep, fy+yoffset, z))
        contractionNode.insert(idx, Node(n0.x+twstep, n0.y, n0.z))

    # mo/muの時、ヒモの上/下の座標を返す
    def overUnder(self, nodeList, index: int, moves: [], l2t: int, side, lr: float):
        for m in moves:
            nz = detourOverUnder
            m = str(m)
            sMove = m.split(' ')
            if sMove[0] == 'mu':
                nz = -nz
            move = sMove[1][:-1]
            if(len(move) == 2):
                move = 't' + move
            (_,node) = self.findNode(side, move)
            nodeList.insert(index, Node(node.x+lr,node.y+l2t*detourOverUnder, node.z))
            nodeList.insert(index, Node(node.x+lr,node.y,node.z+nz))
            nodeList.insert(index, Node(node.x+lr,node.y-l2t*detourOverUnder, node.z))

    # 経路修正した座標値を出力
    def outputNodeRoute(self, node: [], outputFile, isResult=True, hangingNodes = None):
        self.print('hangingNodes: ', hangingNodes)
        for i,n in enumerate(node):
            if i < 3:
                outputFile.write(str(n))
            else:
                isHangingNode = False
                if hangingNodes != None:
                    for ns in hangingNodes:
                        isHangingNode = isHangingNode or (i in ns)
                outputFile.write(n.output_str(isResult, isHangingNode))
            if i < len(node)-1:
                outputFile.write('\n')
        outputFile.close()

    # ヒモのノードなかで指にかかる部分のノードを表示する
    def printNfLRString(self, withContractionNodes=True, title=''):
        global contractionNode
        self.print('###############################', title, '##################################')
        self.print('######## left')
        for idx, n in enumerate(contractionNode):
            if type(n) is Node and n.side=='left':
                self.print(n.dhf, ' :  contractionNode[', idx, ']: ', n.dump())

        self.print('######## right')
        for idx, n in enumerate(contractionNode):
            if type(n) is Node and n.side=='right':
                self.print(n.dhf, ' :  contractionNode[', idx, ']: ', n.dump())
        self.print('###############################', title, '(end) ##################################')

    # contractionNode の中で該当するノードを探す
    # lr : "left"/"right"
    # string: depth+height+finger
    def findNode(self, lr, string):
        for i,n in enumerate(contractionNode):
            if type(n) is Node:
                if n.side == lr and n.dhf == string:
                    return (i,n)
        return None

    def showContractionNode(self, title):
        self.print('--------------------', title, '------------------------------')
        for i,n in enumerate(contractionNode):
            if i>=3:
                self.print(n.dump())
        self.print('--------------------------------------------------')

    def print(self, *arg):
        global debugMode
        if debugMode:
            print(*arg)

    def warning(self, *arg):
        print(*arg)
    


def main(argv):
    global debugMode
    for i,a in enumerate(argv):
        if a == '-debug':
            debugMode = True
            del argv[i]
            break

    if len(argv) < 3 or 3 < len(argv) and len(argv) < 5:
        '''
        print('引数の指定を間違っています．次の2つのコマンドのどちらを指定します')
        print()
        print('    python modifyPath.py <入力経路ファイル名> <経路変更後のファイル名>')
        print('    python modifyPath.py <入力経路ファイル名> <経路変更後のファイル名> <収縮後の経路ファイル名> <剛体周辺を伸ばした後の経路ファイル>')
        print()
        print('なお，入力する経路ファイル名以外はすべて上書き保存するファイル名になります．')
        sys.exit()
        '''
        print('Correct the arguments. Specify one of the following two types of arguments.')
        print('Usage: ')
        print('    python modifyPath.py <original path filename> <altered path filename>')
        print('    python modifyPath.py <original path filename> <altered path filename> <packed path filename> <finger-string extended path filename>')
        print()
        print('Note:')
        print('    o This script modifies the original path file resulting from the simulation')
        print('      by simulator/tutorial_wireWindAndWater.cpp with given finger movement')
        print('      code.')
        print('    o The script first applies a packing algorithm to narrow the space for')
        print('      subsequent simulations. (The result is output to <packed path filename>.)')
        print('    o Next, it extends the finger string. (The result is output to')
        print('      <finger-string extended path filename>.)')
        print('    o It then accepts a finger movement code input and modifies the path')
        print('      accordingly. (The result is output to <altered path filename>.)')
        sys.exit()
    # 経路情報のファイルを読み取る
    # argv （つまりコマンド引数）で経路情報ファイルと，変更後の経路情報ファイルの名前を指定
    routeFile = open(argv[1], 'r')

    # あやとり表記法の中間表現を標準入力から読取
    input = InputStream(sys.stdin.read())
    lexer = IntermediateLexer(input)
    stream = CommonTokenStream(lexer)
    parser = IntermediateParser(stream)

    tree = parser.intermediate()
    walker = ParseTreeWalker()
    listener = MyListener(routeFile)
    # 経路情報を変更（変更のプログラムは上記に書き込む）

    walker.walk(listener, tree)

    # 変更結果を新しいファイルとして保存
    changedRouteFile = open(argv[2], 'w')
    listener.outputNodeRoute(contractionNode ,changedRouteFile)

if __name__ == '__main__':
    main(sys.argv)
