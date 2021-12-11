import maya.cmds as cmds
import importlib


class ToolUI():
    def __init__(self):
        self.window = 'UIWindow'
        pass


    def createWin(self):
        import Orienter
        import renamer
        import ColorChanger
        importlib.reload(renamer)
        importlib.reload(Orienter)
        importlib.reload(ColorChanger)

        self.delete()

        self.window = cmds.window(self.window, title = 'Le Toolbox',widthHeight = (450,200))

        column = cmds.columnLayout(parent = self.window, columnAttach=('both', 5), rowSpacing=10, columnWidth= 450)

        name = cmds.textFieldButtonGrp(label='Naming Scheme', placeholderText='ex. Leg_##_Jnt', buttonLabel='Name',
                                buttonCommand=lambda *x: renamer.rename(cmds.textFieldButtonGrp(name, q=True, text=True)))
        ball = cmds.button(parent=column, label='Ball', command = 'cmds.polySphere()')
        newControll = cmds.button(parent=column, label='New Control',
                    command=lambda x: Orienter.newControll(cmds.colorIndexSliderGrp(col, q=True, value=True)-1))
        col = cmds.colorIndexSliderGrp(label='Select Color', min=0, max=20, value=15,)
        cmds.button(parent=column, label='Apply Color', command=
                    lambda x: ColorChanger.changeColor(cmds.colorIndexSliderGrp(col, q=True, value=True)-1))

        cmds.showWindow(self.window)

    def delete(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)



myUI = ToolUI()
myUI.createWin()
