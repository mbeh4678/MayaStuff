import maya.cmds as cmds

def changeColor(input,ColorShapeNode):
    print(ColorShapeNode)
    colors = ["Clear", "Black", "Dark Grey", "Maroon", "Dark Blue", "Light Blue", "DarkGreen",
              "Purple", "Lavender", "Light Brown", "Brown", "Rust", "Red", "Green", "Blue", "White",
              "Yellow", "Teal", "Seafoam", "Pink"]
    if isinstance(input, str):
        colIndex = colors.index(input)
    else:
        colIndex = input

    items = cmds.ls(selection = True)
    for i in items:
        if ColorShapeNode == 1:
            shape = "".join(cmds.listRelatives(i,shapes = True))
        else:
            shape = i
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", colIndex)




#changeColor(14)


import maya.cmds as cmds


def mirrorControl(ctrl, currentSide='R_', newSide='L_'):
    parent = cmds.listRelatives(ctrl, p=True)[0]
    dup = cmds.duplicate(parent, n=parent.replace(currentSide, newSide))[0]
    sclGrp = cmds.group(em=True, world=True)
    cmds.parent(dup, sclGrp)
    cmds.setAttr(sclGrp + '.sx', - 1)

    try:
        cmds.parent(dup, cmds.listRelatives(parent, p=True)[0])
    except:
        cmds.parent(dup, world=True)
    cmds.delete(sclGrp)

    [cmds.rename(obj, obj.replace(currentSide, newSide)) for obj in cmds.listRelatives(dup, ad=True, s=True)]

for obj in cmds.ls(sl=True):
    mirrorControl(obj, 'R_', 'L_')