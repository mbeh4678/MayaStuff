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