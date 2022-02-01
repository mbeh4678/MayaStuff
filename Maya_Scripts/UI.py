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

        self.window = cmds.window(self.window, title='Le Toolbox', widthHeight=(450, 2500))

        column = cmds.columnLayout(parent=self.window, columnAttach=('both', 5), rowSpacing=10, columnWidth=450)

        name = cmds.textFieldButtonGrp(label='Naming Scheme', placeholderText='ex. Leg_##_Jnt', buttonLabel='Name',
                                       buttonCommand=lambda *x: renamer.rename(
                                           cmds.textFieldButtonGrp(name, q=True, text=True)))
        ball = cmds.button(parent=column, label='Ball', command='cmds.polySphere()')
        newControll = cmds.button(parent=column, label='New Control',
                                  command=lambda x: Orienter.newControll(
                                      cmds.colorIndexSliderGrp(col, q=True, value=True) - 1))
        col = cmds.colorIndexSliderGrp(label='Select Color', min=0, max=20, value=15, )
        cmds.button(parent=column, label='Apply Color', command=
        lambda x: ColorChanger.changeColor(cmds.colorIndexSliderGrp(col, q=True, value=True) - 1))

        cmds.button(parent=column, label='Show Joint Orient', command=lambda *x: self.display_joint_orient())
        cmds.button(parent=column, label='Replace', command=lambda *x: self.replaceObject())
        cmds.button(parent=column, label='Constrain', command=lambda *x: self.constrain())

        cmds.showWindow(self.window)

    def delete(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

    #   myUI = ToolUI()
    #   myUI.createWin()

    def display_joint_orient(self):
        sels = cmds.ls(sl=True)

        for sel in sels:
            if cmds.nodeType(sel) == 'joint':
                state = cmds.getAttr(f'{sel}.displayLocalAxis')
                cmds.setAttr(f'{sel}.displayLocalAxis', not state)
                cmds.setAttr(f'{sel}.jointOrientX', keyable=not state, channelBox=not state)
                cmds.setAttr(f'{sel}.jointOrientX', keyable=not state, channelBox=not state)
                cmds.setAttr(f'{sel}.jointOrientX', keyable=not state, channelBox=not state)

    #   display_joint_orient()

    def replaceObject(self):
        sels = cmds.ls(sl=True)
        newName = sels[1]
        newParent = cmds.listRelatives(sels[1], parent=True)
        cmds.parent(sels[0], newParent)
        cmds.delete(sels[1])
        cmds.rename(sels[0], newName)

    def constrain(self):

        sels = cmds.ls(sl=True)

        constraint_target = sels[0]
        ctrl = sels[1]
        ctrl_grp = cmds.listRelatives(ctrl, parent=True)[0]

        # Creating separate parent constraints for translate and rotate
        t_constraint = cmds.parentConstraint(constraint_target, ctrl_grp, maintainOffset=True,
                                             skipRotate=['x', 'y', 'z'], weight=1)[0]
        r_constraint = cmds.parentConstraint(constraint_target, ctrl_grp, maintainOffset=True,
                                             skipTranslate=['x', 'y', 'z'], weight=1)[0]

        # Adding custom attributes to control
        cmds.addAttr(ctrl, longName='FollowTranslate', attributeType='double', min=0, max=1, defaultValue=1)
        cmds.setAttr(f'{ctrl}.FollowTranslate', e=True, keyable=True)

        cmds.addAttr(ctrl, longName='FollowRotate', attributeType='double', min=0, max=1, defaultValue=1)
        cmds.setAttr(f'{ctrl}.FollowRotate', e=True, keyable=True)

        cmds.connectAttr(f'{ctrl}.FollowTranslate', f'{t_constraint}.w0', force=True)
        cmds.connectAttr(f'{ctrl}.FollowRotate', f'{r_constraint}.w0', force=True)