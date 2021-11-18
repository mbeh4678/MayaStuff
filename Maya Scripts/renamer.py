import maya.cmds as cmds


scheme = "Leg_####_Jnt"
items = cmds.ls(selection = True)
count = 0
tags = int(scheme.count("#"))
scheme = scheme.partition("#"*tags)

print(scheme)
for count, i in enumerate(items,start=1):
    cmds.rename(i,f"{scheme[0]+str(count).zfill(tags)+scheme[-1]}")



