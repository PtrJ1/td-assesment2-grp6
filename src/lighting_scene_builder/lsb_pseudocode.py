#This program will allow the user to import assets into Maya and add lighting options to the model
#in order to create a render scene.

import maya.cmds as mc #Import Maya Commands

def setImport(): #Create import function
    setImportPath = 'X:/Path_To_File.fbx' #Import model from = 'This Location'
    cmds.file(setImportPath, i=True, mergeNamespacesOnClash=True, namespace=':');

setImport()

modelEditor(getPanel(withFocus = True), edit = True, displayLights = 'all') #Create light functions

modelEditor(getPanel(withFocus = True), edit = True, shadows = True) #Create shadows

shadingNode('directionalLight', asLight = True) #Create Directional Light
directionalLight (n = 'Light1') #Set up intensity of the light
setAttr('Light1.intensity', 4) #Set up Input for intensity adjustment
setAttr('Light1.useDepthMapShadows', 1) #Make shadows more smooth
setAttr('Light1.color', 0, 0.5, 0.5, type = 'double3') #Add colour to lighting

setAttr('Light1.rotateX', -90) #Rotate at X-axis
setAttr('Light1.rotateY', -90) #Rotate at Y-axis
setAttr('Light1.rotateZ', -90) #Rotate at Z-axis
