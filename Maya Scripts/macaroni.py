

import maya.cmds as cmds

for k in range(3):
    for i in range(3):
        cmds.polySphere(radius=100-i*20, subdivisionsX=20, subdivisionsY=20,
                        name=f"Snowman {k+1} Body {i+1}")
        cmds.move(0, i*100, 0)
        if i < 2:
            cmds.polyCylinder(radius=10, height=5,sx=20,sy=1,sz=1,ax=(1,0,0)
                              ,name=f"Snowman {k+1} Button {i+1}")
            cmds.move(100 - i*20,i*100,0,relative=True)
    cmds.polyCone(radius=10,height=100,sx=20,ax=(1,0,0),
                  name=f"Snowman {k+1} Nose")
    cmds.move(80,200,0,relative=True)
    cmds.polyCylinder(r=40,h=5,sx=20,sz=2,ax=(0,1,0),
                      name = f"Snowman {k+1} Hat")
    cmds.move(0,250,0,relative=True)
    cmds.select(f"Snowman_{k+1}_Hat.f[80:99]",replace=True)
    #cmds.scale(0,34,0,r=True,pivot=(-1.90735e-06, 252.5, -3.8147e-06))
    cmds.polyExtrudeFacet(f"Snowman_{k+1}_Hat.f[80:99]",kft=True, ltz=20)
    cmds.select(f"Snowman_{k+1}_*",r=True)
    cmds.move(0,0,k*150,r=True)