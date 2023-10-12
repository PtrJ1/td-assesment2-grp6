import maya.cmds as cmds

path="C:/Example/"

#Export File
cmds.file(path + "new-lighting", force=True, typ="mayaBinary", exportSelected=True)

#Import File
cmds.file("assets/Lighting/new-lighting.ma", i=True)
