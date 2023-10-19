import maya.cmds as cmds

def createCamera():
    cameraName = cmds.camera(horizontalFilmAperture=1.247, verticalFilmAperture=0.702, farClipPlane=100000)
    setResolutionWidth = cmds.setAttr('defaultResolution.width', 1920)
    setResolutionHeight = cmds.setAttr('defaultResolution.height', 1080)
    setDeviceAspectRatio = cmds.setAttr('defaultResolution.deviceAspectRatio', 1.778)

def alexaCamera():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".horizontalFilmAperture", 1.247)
            cmds.setAttr(cam_shp[0]+".verticalFilmAperture", 0.702)
            cmds.setAttr(cam_shp[0]+".farClipPlane", 100000)
            
    setResolutionWidth = cmds.setAttr('defaultResolution.width', 1920)
    setResolutionHeight = cmds.setAttr('defaultResolution.height', 1080)
    setDeviceAspectRatio = cmds.setAttr('defaultResolution.deviceAspectRatio', 1.778)


def focalLength12():
    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 12)


def focalLength14():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 14)
                        
def focalLength16():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 16)
            
def focalLength18():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 18)
            
def focalLength21():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 21)
            
def focalLength25():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 25)
            
def focalLength27():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 27)
            
def focalLength32():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 32)
            
def focalLength35():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 35)
            
def focalLength40():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 40)
            
def focalLength50():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 50)
            
def focalLength65():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 65)
            
def focalLength75():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 75)
            
def focalLength100():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 100)
            
def focalLength135():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 135)
            
def focalLength150():

    for each_cam_tf in cmds.ls(sl=True):
        cam_shp = cmds.listRelatives(each_cam_tf,type="camera")
        if cam_shp:
            cmds.setAttr(cam_shp[0]+".fl", 150)

def cameraTools():
    
    if cmds.window('cameraTools', exists = True):
        cmds.deleteUI('cameraTools')
        
    cmds.window('cameraTools', resizeToFitChildren=True)

    cmds.columnLayout()
    
    cmds.separator(h=10)
    cmds.text('PREVIS: Creates an AlexaLF camera')
    cmds.text('Sets the correct render settings')
    cmds.separator(h=10)
    
    cmds.button(label = 'Create Camera', command = 'createCamera()')


    cmds.separator(h=30)
    cmds.text('LAYOUT: Sets AlexaLF Settings')
    cmds.separator(h=10)
    
    cmds.button(label = 'AlexaLF Settings', command = 'alexaCamera()')
    

    cmds.separator(h=30)
    cmds.text('Sets focal length on selected cameras')
    cmds.separator(h=10)
    
    cmds.button(label = '12mm', command = 'focalLength12()')
    cmds.separator(h=10)
    cmds.button(label = '14mm', command = 'focalLength14()')
    cmds.separator(h=10)
    cmds.button(label = '16mm', command = 'focalLength16()')
    cmds.separator(h=10)
    cmds.button(label = '18mm', command = 'focalLength18()')
    cmds.separator(h=10)
    cmds.button(label = '21mm', command = 'focalLength21()')
    cmds.separator(h=10)
    cmds.button(label = '25mm', command = 'focalLength25()')
    cmds.separator(h=10)
    cmds.button(label = '27mm', command = 'focalLength27()')
    cmds.separator(h=10)
    cmds.button(label = '32mm', command = 'focalLength32()')
    cmds.separator(h=10)
    cmds.button(label = '35mm', command = 'focalLength35()')
    cmds.separator(h=10)
    cmds.button(label = '40mm', command = 'focalLength40()')
    cmds.separator(h=10)
    cmds.button(label = '50mm', command = 'focalLength50()')
    cmds.separator(h=10)
    cmds.button(label = '65mm', command = 'focalLength65()')
    cmds.separator(h=10)
    cmds.button(label = '75mm', command = 'focalLength75()')
    cmds.separator(h=10)
    cmds.button(label = '100mm', command = 'focalLength100()')
    cmds.separator(h=10)
    cmds.button(label = '135mm', command = 'focalLength135()')
    cmds.separator(h=10)
    cmds.button(label = '150mm', command = 'focalLength150()')
    cmds.separator(h=10)
    
    cmds.showWindow('cameraTools')

    
cameraTools()
