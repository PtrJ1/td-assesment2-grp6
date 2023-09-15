import maya.cmds as mc #Code set up

mc.polyPlane (w = 20, h = 20) #Create Plane (Width, Height)
mc.polyCube (name = 'cube') #Create Cube (Cube Name)

modelEditor(getPanel(withFocus = True), edit = True, displayLights = 'all') #Initiate light functions

modelEditor(getPanel(withFocus = True), edit = True, shadows = True) #Create shadows

shadingNode('directionalLight', asLight = True) #Create Directional Light
directionalLight (n = 'Light1') #Sets up intensity of the light
setAttr('Light1.intensity', 4) #Input for inensity adjustment
setAttr('Light1.useDepthMapShadows', 1) #Make shadows more smooth
setAttr('Light1.color', 0, 0.5, 0.5, type = 'double3') #Add colour to lighting

setAttr('Light1.rotateX', -90) #Rotate at X-axis
setAttr('Light1.rotateY', -90) #Rotate at Y-axis
setAttr('Light1.rotateZ', -90) #Rotate at Z-axis
