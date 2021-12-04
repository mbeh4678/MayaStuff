import maya.cmds as cmds
import ColorChanger
import importlib
importlib.reload(ColorChanger)


def Orienter(color):

    targets = cmds.ls(selection = True)
    if len(targets) == 0 :
        print('0')
    else:
        for t in targets:
            baseName = str(next(i for i in t.rpartition('_') if i))
            print(baseName)
            ctrl = cmds.circle(normal = (0,1,0), name = f"{baseName}_Ctrl")[0]
            grp = cmds.group(ctrl, name = f"{baseName}_Ctrl_Grp")
            cmds.matchTransform(grp,t)
            cmds.select(ctrl, replace = True)
            ColorChanger.changeColor(color)


Orienter(8)