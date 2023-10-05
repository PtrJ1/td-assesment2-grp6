import maya.cmds as cmds

class Window(object):
        
    #constructor
    def __init__(self):
            
        self.window = "Window"
        self.title = "Lighting Manager"
        self.size = (400, 400)
            
        # close old window is open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout(adjustableColumn = True)
        
        cmds.text(self.title)
        cmds.separator(height=20)
        
        self.cubeName = cmds.textFieldGrp(label='Cube Name:')
        self.cubeSize = cmds.floatFieldGrp(numberOfFields=3, label='Size:',
                        value1=1, value2=1, value3=1)
                        
        self.cubeSubdivs = cmds.intSliderGrp(field=True, label='Subdivs',
                        minValue=1, maxValue=10, value=1)

        self.cubeCreateBtn = cmds.button(label='Create Cube')
        
        #display new window
        cmds.showWindow()

def createCube(self, *args):
    
    name = cmds.textFieldGrp(self.cubeName, query=True, text=True)  
    
    width = cmds.floatFieldGrp(self.cubeSize, query=True, text=True)
    height = cmds.floatFieldGrp(self.cubeName, query=True, text=True)
    depth = cmds.floatFieldGrp(self.cubeName, query=True, text=True)
    
    subdivs = cmds.intSliderGrp(self.cubeSubdivs, query=True, value=True)
    
    cmds.polyCube(name=name, width=width, height=height, depth=depth,
    subdivisionsWidth = subdivs, subdivisionsHeight = subdivs, subdivisionsDepth = subdivs)
                                   
myWindow = Window()
