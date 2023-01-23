import sys
import vpython as vs
import numpy as np

def readFile(ioFile, inputNode):
    for i,n in enumerate(ioFile):
        n = n.strip()
        # 0~2行目は座標値ではないためスキップ
        if i < 3:
            continue
        # 指を表す記号ならスキップ
        if n.startswith('R') or n.startswith('L'):
            continue
        # 座標値をリストとして格納
        vec3 = pointSplit(n)
        inputNode.append(vec3)

def pointSplit(line :str):
    line = line[1:len(line)-1]
    spl = line.split(',')
    x :float= -float(spl[0])
    y :float= -float(spl[1])
    z :float= float(spl[2])
    bp = '' if len(spl)<=3 else spl[3]
    memo :str= line
    return x,y,z,bp,memo

def drawSegment(m, n):  # m, n はともに長さ3の配列，mからnに線分を描く
    vs.cylinder(pos=vs.vector(m[0], m[1], m[2]),
        axis=vs.vector(n[0]-m[0], n[1]-m[1], n[2]-m[2]),
        radius=0.005, color=vs.color.white)

def init_camera():
    vs.scene.center = vs.vector(0,0,0)
    vs.scene.forward = vs.vector(0,0,-1)
    vs.scene.range = 1.5 

def main(argv):
    if len(argv) < 2:
        print('path file is expected.')
        print('Usage:')
        print('    python simple_viewer.py <path file>')
        sys.exit()

    # 経路情報のファイルを読み取る
    # argv （つまりコマンド引数）で経路情報ファイルと，変更後の経路情報ファイルの名前を指定
    routeFile = open(argv[1], 'r')
    stringRouteNode = []
    
    readFile(routeFile, stringRouteNode)
    
    spheres = []
    init_camera()

    memodict = {}
    #########################
    # vpython を利用した描画
    first = None
    last = None
    #hue = vs.color.rgb_to_hsv(vs.color.orange)[0]
    hue = 0.1       # orange
    cdict = {}
    for i,n in enumerate(stringRouteNode):
        if i==0:
            cl = vs.color.red
        elif n[3] != '':
            if n[3] in cdict:
                h = cdict[n[3]]
            else:
                h = hue
                cdict[n[3]] = h
                hue = (hue + 0.17) % 1
            cl = vs.color.hsv_to_rgb(vs.vector(h, 1, 1))
        else:
            cl = vs.color.blue
        sp = vs.sphere(pos=vs.vector(n[0], n[1], n[2]), radius=0.01, color=cl)
        memodict[sp] = n[4]
        spheres.append(sp)
        if first == None:
            first = n   # 開始点（ループ終了後に最後の点と結ぶのに使う
        if last!=None:
            drawSegment(last, n)
        last = n
    if first != None and last != None:
        drawSegment(last, first)
    print(cdict)


    currentSphere = None
    while True:
        ev = vs.scene.waitfor('click keydown')
        if ev.event == 'click':
            #print("ev.pos = ", ev.pos)
            if currentSphere != None:
                currentSphere.color=vs.color.blue
            for i,sp in enumerate(spheres):
                d = (sp.pos.x-ev.pos.x)**2 + (sp.pos.y-ev.pos.y)**2
                if d <= 0.002:
                    currentSphere = sp
                    currentSphere.color = vs.color.red
                    print(i+3, ':', memodict[sp])
        else:
            if ev.key==' ':
                init_camera()

if __name__ == '__main__':
    main(sys.argv)
