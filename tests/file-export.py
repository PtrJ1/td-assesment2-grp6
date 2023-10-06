import maya.cmds as cmds

path="C:/Example/"

cmds.file(path + "new-lighting", force=True, typ="mayaBinary", exportSelected=True)
