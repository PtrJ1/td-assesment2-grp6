import maya.cmds as cmds

path="C:/Users/13604677/Desktop/Lighting-File/"

cmds.file(path + "new-lighting", force=True, typ="mayaBinary", exportSelected=True)

class Window(object):
        
    def __init__(self):
            
        self.window = "Window"
        self.title = "Light Exporter"
        self.size = (200, 100)
            
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout(adjustableColumn = True)

        cmds.button(label='Import')
        cmds.separator(h=10)
        cmds.button(label='Export')
        
        cmds.showWindow()

                                   
myWindow = Window()
