import maya.cmds as cmds


def joints_from_sels():
    sels = cmds.ls(sl=True)

    for sel in sels:

        pos = cmds.xform(sel, q=True, rotatePivot = True, ws=True)
        cmds.select(cl=True)
        jnt = cmds.joint(position=[0,0,0], absolute=True)

        cmds.xform(jnt, translation = pos, ws=True)

def parent_from_sels():
    sels= smds.ls(sl=True)

    for i, sel in enumerate(sels):
        cmds.parent(sels[i], sels[i+1])