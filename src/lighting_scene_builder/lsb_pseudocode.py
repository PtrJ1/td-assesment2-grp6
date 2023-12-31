#This program will allow the user to import an asset into Maya and add lighting options to the model
#in order to create a render scene.

import maya.cmds as cmds

create GUI window with buttons and logs

def setImport():
    setImportPath = 'X:\Path_To_File.fbx'
    cmds.file(setImportPath, i=True, mergeNamespacesOnClash=True, namespace=':');
    
    setImport()

def buttonMethod(args):
    cmds.PolyCube()

def showUI():
    window = cmds.window(title="Lighting Manager", widthHeight = (500, 500)
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.rowlayout(adjustableColumn3, numberOfColumns=4)
    cmds.button(label="Create"' command = buttonMethod)
    cmds.button(label="Save", command = buttonMethod)
    cmds.button(label="Import", command = buttonMethod)
    cmds.button(label="Refresh", command = buttonMethod)
    
cmds.showWindow(window)

modelEditor(getPanel(withFocus = True), edit = True, displayLights = 'all')

modelEditor(getPanel(withFocus = True), edit = True, shadows = True)

shadingNode('directionalLight', asLight = True)
directionalLight (n = 'Light1')
setAttr('Light1.intensity', 4)
setAttr('Light1.useDepthMapShadows', 1)
setAttr('Light1.color', 0, 0.5, 0.5, type = 'double3')

setAttr('Light1.rotateX', -90)
setAttr('Light1.rotateY', -90)
setAttr('Light1.rotateZ', -90)
                
