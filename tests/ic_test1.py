import pymel.core as pm
import maya.cmds as cmds
import maya.OpenMaya as om


# GUI Initialization
def main():
    window = pm.window(title="Integrity Check Tool", widthHeight=(200, 150))
    layout = pm.columnLayout(adjustableColumn=True)
    pm.button(label='Run Integrity Check', command=runIntegrityCheck)
    pm.textScrollList("logArea", numberOfRows=8, allowMultiSelection=True, append=["Integrity Log will appear here..."])
    pm.showWindow(window)

def runIntegrityCheck(*args):
    pm.textScrollList("logArea", edit=True, removeAll=True)
    # General Checks
    if not removeUnknownOrUnusedNodes():
        log_message("Unknown or unused nodes found.")
    if not isAssetNamingConventionValid():
        log_message("Asset naming convention error.")
    if not isNodeHierarchyValid():
        log_message("Node hierarchy error.")
    if not areReferencesValid():
        log_message("Reference error.")
    checkAttributesForNaN()

    # Context Specific Checks
    # Placeholder for context detection
    context = "Layout"  # placeholder
    if context == "Layout":
        if not isCameraApertureValid():
            log_message("Aperture error.")
        if not isFocalLengthAndFStopValid():
            log_message("Invalid focal length or f-stop.")
    elif context in ["SetPieces", "Sets"]:
        if not isTransformAndPivotAtOrigin():
            log_message("Transform/Pivot error.")
        if context == "Sets" and not isLatestVersionOfSetPiece():
            log_message("Outdated setPiece.")

def log_message(message):
    pm.textScrollList("logArea", edit=True, append=[message])

def removeUnknownOrUnusedNodes():
    FOUND = False
    
    # Get all nodes in the scene
    all_nodes = cmds.ls(dag=True, long=True)
    
    # List of default nodes that should not be deleted
    default_nodes = ["time1", "sequenceManager1", "hardwareRenderingGlobals", "renderPartition", 
                     "renderGlobalsList1", "defaultLightList1", "defaultShaderList1", "postProcessList1", 
                     "defaultRenderUtilityList1", "defaultRenderingList1", "lightList1", "defaultTextureList1", 
                     "lambert1", "standardSurface1", "particleCloud1", "initialShadingGroup", "initialParticleSE", 
                     "initialMaterialInfo", "shaderGlow1", "dof1", "defaultRenderGlobals", "defaultRenderQuality", 
                     "defaultResolution", "defaultLightSet", "defaultObjectSet", "defaultViewColorManager", 
                     "defaultColorMgtGlobals", "hardwareRenderGlobals", "characterPartition", 
                     "defaultHardwareRenderGlobals", "ikSystem", "hyperGraphInfo", "hyperGraphLayout", 
                     "globalCacheControl", "strokeGlobals", "dynController1", "perspShape", "persp", 
                     "topShape", "top", "frontShape", "front", "sideShape", "side", "layerManager", 
                     "lightLinker1", "shapeEditorManager", "poseInterpolatorManager", "defaultLayer", 
                     "renderLayerManager", "defaultRenderLayer"]
    
    for node in all_nodes:
        # Check if the node is not in the default nodes list
        if node not in default_nodes:
            try:
                if cmds.nodeType(node) in ["unknown", "unknownDag", "unknownTransform"]:
                    cmds.delete(node)
                    FOUND = True
            except Exception as e:
                # Log the error without terminating the entire script
                om.MGlobal.displayError(str(e))
    
    return not FOUND

def isAssetNamingConventionValid():
    # Placeholder naming convention
    def naming_convention(name):
        return "asset_" in name
    
    for asset in pm.ls(dag=True):
        if not naming_convention(asset.name()):
            return False
    return True

def isNodeHierarchyValid():
    # Placeholder for hierarchy validation
    for node in pm.ls(dag=True):
        if "invalid_condition" in node.name():  # Replace later
            return False
    return True

def areReferencesValid():
    # Placeholder for references validation
    for ref in pm.listReferences():
        if not ref.isLoaded():
            return False
    return True

def checkAttributesForNaN():
    for node in pm.ls(dag=True, type="transform"):
        for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]:
            val = node.getAttr(attr)
            if abs(val) < 0.0001:  # Placeholder for NaN check
                node.setAttr(attr, round(val, 4))

def isCameraApertureValid():
    for cam in pm.ls(type="camera"):
        if cam.getAttr("aspectRatio") != 16/9.0:
            return False
    return True

def isFocalLengthAndFStopValid():
    valid_focal_lengths = ["12", "14", "16", "18", "21", "25", "27", "32", "35", "40", "50", "65", "75", "100", "135", "150"]
    valid_f_stops = ["1.3", "2", "2.8", "4", "5.6", "8", "11", "16", "22"]
    
    for cam in pm.ls(type="camera"):
        if str(cam.getAttr("focalLength")) not in valid_focal_lengths or str(cam.getAttr("fStop")) not in valid_f_stops:
            return False
    return True

def isTransformAndPivotAtOrigin():
    for node in pm.ls(dag=True, type="transform"):
        pivot = pm.xform(node, query=True, worldSpace=True, pivot=True)
        if node.getTranslation(space="world") != (0,0,0) or (pivot[0], pivot[1], pivot[2]) != (0,0,0):
            return False
    return True

def isLatestVersionOfSetPiece():
    # Placeholder for latest version check
    for ref in pm.listReferences():
        if "old_version" in ref.path:  # Replace later
            return False
    return True

main()
