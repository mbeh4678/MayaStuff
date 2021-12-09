import maya.cmds as cmds
import Orienter
import importlib
importlib.reload(Orienter)


class ToolUI():
    def __init__(self):
        self.window = 'UIWindow'
        pass


    def createWin(self):
        self.delete()

        self.window = cmds.window(self.window, title = 'UI Window',
                                  widthHeight = (200,55))

        column = cmds.columnLayout(parent = self.window, adjustableColumn = True)
        cmds.button(parent = column, label = 'Ball', command = 'cmds.polySphere()')
        #cmds.button(parent = column, label = 'Red Color', command = lambda x: Orienter.newControll(13))
        cmds.button(parent = column)

        cmds.showWindow(self.window)

    def delete(self):
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window)





myUI = ToolUI()
myUI.createWin()
