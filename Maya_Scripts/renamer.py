import maya.cmds as cmds

def rename(scheme): #example scheme:


    items = cmds.ls(selection = True)
    count = 0
    tags = int(scheme.count("#"))
    scheme = scheme.partition("#"*tags)

    for count, i in enumerate(items,start=1):
        cmds.rename(i,f"{scheme[0]+str(count).zfill(tags)+scheme[-1]}")



