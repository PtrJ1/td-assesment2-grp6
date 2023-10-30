import pymel.core as pm
import maya.cmds as cmds
import maya.OpenMaya as om
import re


# GUI Initialization
def main():
    if pm.window("integrityCheckerWin", exists=True):
        pm.deleteUI("integrityCheckerWin")
    
    window = pm.window("integrityCheckerWin", title="Integrity Checker", widthHeight=(600, 400))
    
    mainLayout = pm.rowLayout(numberOfColumns=2, adjustableColumn=2, columnAttach=(1, 'right', 5), columnWidth=[(1, 230), (2, 250)])
    
    # COLUMN 1: Checks
    checksColumn = pm.columnLayout(parent=mainLayout, adjustableColumn=True, rowSpacing=5, columnOffset=('both', 10))
    
    # General Section
    pm.text(label="General", height=25, font='boldLabelFont')
    pm.checkBox("chk_unknownNodes", label="Unknown/Unused Nodes")
    pm.checkBox("chk_assetNames", label="Asset Names")
    pm.checkBox("chk_nodeHierarchy", label="Node Hierarchy")
    pm.checkBox("chk_referenceErrors", label="Reference Errors")
    pm.checkBox("chk_nanAttributes", label="NaN Attributes")
    
    
    pm.separator(style='none', height=10)
    
    # Layout Section
    pm.text(label="Layout", height=25, font='boldLabelFont')
    pm.checkBox("chk_cameraAperture", label="Camera Aperture")
    pm.checkBox("chk_focalLength", label="Focal Length/f-stop")
    
    
    pm.separator(style='none', height=10)
    
    # setPieces Section
    pm.text(label="setPieces", height=25, font='boldLabelFont')
    pm.checkBox("chk_transformPivotSetPieces", label="Transform and Pivot")
    
    
    pm.separator(style='none', height=10)
    
    # set Section
    pm.text(label="sets", height=25, font='boldLabelFont')
    pm.checkBox("chk_transformPivotSet", label="Transform and Pivot")
    pm.checkBox("chk_referenceVersion", label="Reference Version")
    
    pm.separator(style='none', height=20)
    pm.button(label="Run selected checks", command=runSelectedChecks)
    
    # COLUMN 2: Logs
    logsColumn = pm.columnLayout(parent=mainLayout, adjustableColumn=True, rowSpacing=5, columnOffset=('both', 10))
    pm.textScrollList("logArea", numberOfRows=20, allowMultiSelection=True, append=["Integrity Log will appear here..."], width=230, height=330)
    pm.separator(style='none', height=10)
    pm.button(label="Run all checks", command=runIntegrityCheck)
    
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
            

def runSelectedChecks(*args):
    pm.textScrollList("logArea", edit=True, removeAll=True)
    
    if pm.checkBox("chk_unknownNodes", query=True, value=True) and not removeUnknownOrUnusedNodes():
        log_message("Unknown or unused nodes found.")
    if pm.checkBox("chk_assetNames", query=True, value=True) and not isAssetNamingConventionValid():
        log_message("Asset naming convention error.")
    if pm.checkBox("chk_nodeHierarchy", query=True, value=True) and not isNodeHierarchyValid():
        log_message("Node hierarchy error.")
    # ... rest of the checks

    # Context detection not yet implemented 
    context = "Layout"  # placeholder
    if context == "Layout" and pm.checkBox("chk_cameraAperture", query=True, value=True) and not isCameraApertureValid():
        log_message("Aperture error.")
    # ... rest of checks


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
    naming_convention_pattern = re.compile(r'^asset_[A-Za-z0-9]+(_v\d{3})?$')
    
    all_valid = True
    for asset in pm.ls(dag=True):
        asset_name = asset.name()
        if not naming_convention_pattern.match(asset_name):
            log_message(f"Asset naming convention error for: {asset_name}")
            all_valid = False
    return all_valid

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
