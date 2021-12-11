import maya.cmds as cmds
import ColorChanger
import importlib
importlib.reload(ColorChanger)


def newControll(color):

    targets = cmds.ls(selection = True)
    if len(targets) == 0 :
        print('0')
    else:
        for t in targets:
            if int(t.count('_')) > 1:
                print('partition ' + t)
                baseName = str(next(i for i in t.rpartition('_') if i))
            else:
                baseName = t
            print(int(t.count('#')))
            ctrl = cmds.circle(normal = (0,1,0), name = f"{baseName}_Ctrl")[0]
            grp = cmds.group(ctrl, name = f"{baseName}_Ctrl_Grp")
            cmds.matchTransform(grp,t)
            cmds.select(ctrl, replace = True)
            ColorChanger.changeColor(color)


