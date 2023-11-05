import pymel.core as pm
import maya.cmds as cmds
import maya.OpenMaya as om
import re
import math
import os

ui_elements = {}
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
    ui_elements['unknownNodes'] = pm.checkBox("chk_unknownNodes", label="Unknown/Unused Nodes")
    ui_elements['assetNames'] = pm.checkBox("chk_assetNames", label="Asset Names")
    ui_elements['nodeHierarchy'] = pm.checkBox("chk_nodeHierarchy", label="Node Hierarchy")
    ui_elements['refernceErrors'] = pm.checkBox("chk_referenceErrors", label="Reference Errors")
    ui_elements['nanAttributes'] = pm.checkBox("chk_nanAttributes", label="NaN Attributes")
    
    
    pm.separator(style='none', height=10)
    
    # Layout Section
    pm.text(label="Layout", height=25, font='boldLabelFont')
    ui_elements['cameraAperture'] = pm.checkBox("chk_cameraAperture", label="Camera Aperture")
    ui_elements['focalLength'] = pm.checkBox("chk_focalLength", label="Focal Length/f-stop")
    
    
    pm.separator(style='none', height=10)
    
    # setPieces Section
    pm.text(label="setPieces", height=25, font='boldLabelFont')
    ui_elements['transformPivotSP'] = pm.checkBox("chk_transformPivotSetPieces", label="Transform and Pivot")
    
    
    pm.separator(style='none', height=10)
    
    # set Section
    pm.text(label="sets", height=25, font='boldLabelFont')
    ui_elements['tranformPivot'] = pm.checkBox("chk_transformPivotSet", label="Transform and Pivot")
    ui_elements['referenceVer'] = pm.checkBox("chk_referenceVersion", label="Reference Version")
    
    pm.separator(style='none', height=20)
    pm.button(label="Run selected checks", command=runSelectedChecks)
    
    # COLUMN 2: Logs
    logsColumn = pm.columnLayout(parent=mainLayout, adjustableColumn=True, rowSpacing=5, columnOffset=('both', 10))
    pm.textScrollList("logArea", numberOfRows=20, allowMultiSelection=True, append=["Integrity Log will appear here..."], width=230, height=330)
    pm.separator(style='none', height=10)
    pm.button(label="Run all checks", command=runIntegrityCheck)
    
    pm.showWindow(window)

def set_label_color(check_name, success):
    if success:
        color = (0, 1, 0)  # Green
    else:
        color = (1, 0, 0)  # Red
    
    pm.checkBox(ui_elements[check_name], edit=True, bgc=color)


def runIntegrityCheck(*args):
    pm.textScrollList("logArea", edit=True, removeAll=True)
    result_unknownNodes = removeUnknownOrUnusedNodes()
    set_label_color('unknownNodes', result_unknownNodes)
    if not result_unknownNodes:
        log_message("Unknown or unused nodes found.")
        
    
    # Check for Asset Naming Convention
    result_assetNames = isAssetNamingConventionValid()
    set_label_color('assetNames', result_assetNames)
    if not result_assetNames:
        log_message("Asset naming convention error.")
        
    # Check for Node Hierarchy
    result_nodeHierarchy = isNodeHierarchyValid()
    set_label_color('nodeHierarchy', result_nodeHierarchy)
    if not result_nodeHierarchy:
        log_message("Node hierarchy error.")
        
    # Check for Reference Errors
    result_referenceErrors = areReferencesValid()
    set_label_color('refernceErrors', result_referenceErrors)
    if not result_referenceErrors:
        log_message("Reference error.")
        
    # Check for NaN Attributes
    result_nanAttributes = checkAttributesForNaN()
    set_label_color('nanAttributes', result_nanAttributes)
    if not result_nanAttributes:
        log_message("Found NaN or infinite values in node attributes.")
        
    # Check for Camera Aperture
    result_cameraAperture = isCameraApertureValid()
    set_label_color('cameraAperture', result_cameraAperture)
    if not result_cameraAperture:
        log_message("Aperture error.")
        
    # Check for Focal Length/f-stop
    result_focalLength = isFocalLengthAndFStopValid()
    set_label_color('focalLength', result_focalLength)
    if not result_focalLength:
        log_message("Invalid focal length or f-stop.")
        
    # Check for Transform and Pivot in SetPieces
    result_transformPivotSetPieces = isTransformAndPivotAtOrigin()
    set_label_color('transformPivotSP', result_transformPivotSetPieces)
    if not result_transformPivotSetPieces:
        log_message("Transform/Pivot error.")
        
    # Check for Latest Version of Set Piece
    result_referenceVersion = isLatestVersionOfSetPiece()
    set_label_color('referenceVer', result_referenceVersion)
    if not result_referenceVersion:
        log_message("Outdated setPiece.")

            

def runSelectedChecks(*args):
    pm.textScrollList("logArea", edit=True, removeAll=True)
    
    if pm.checkBox("chk_unknownNodes", query=True, value=True):
        result_unknownNodes = removeUnknownOrUnusedNodes()
        set_label_color('unknownNodes', result_unknownNodes)
        if not result_unknownNodes:
            log_message("Unknown or unused nodes found.")
    
    if pm.checkBox("chk_assetNames", query=True, value=True):
        result_assetNames = isAssetNamingConventionValid()
        set_label_color('assetNames', result_assetNames)
        if not result_assetNames:
            log_message("Asset naming convention error.")
        
    if pm.checkBox("chk_nodeHierarchy", query=True, value=True):
        result_nodeHierarchy = isNodeHierarchyValid()
        set_label_color('nodeHierarchy', result_nodeHierarchy)
        if not result_nodeHierarchy:
            log_message("Node hierarchy error.")
        
    if pm.checkBox("chk_referenceErrors", query=True, value=True):
        result_referenceErrors = areReferencesValid()
        set_label_color('refernceErrors', result_referenceErrors)
        if not result_referenceErrors:
            log_message("Reference error.")
        
    if pm.checkBox("chk_nanAttributes", query=True, value=True):
        result_nanAttributes = checkAttributesForNaN()
        set_label_color('nanAttributes', result_nanAttributes)
        if not result_nanAttributes:
            log_message("Found NaN or infinite values in node attributes.")
        
    if pm.checkBox("chk_cameraAperture", query=True, value=True):
        result_cameraAperture = isCameraApertureValid()
        set_label_color('cameraAperture', result_cameraAperture)
        if not result_cameraAperture:
            log_message("Aperture error.")
        
    if pm.checkBox("chk_focalLength", query=True, value=True):
        result_focalLength = isFocalLengthAndFStopValid()
        set_label_color('focalLength', result_focalLength)
        if not result_focalLength:
            log_message("Invalid focal length or f-stop.")
        
    if pm.checkBox("chk_transformPivotSetPieces", query=True, value=True):
        result_transformPivotSetPieces = isTransformAndPivotAtOrigin()
        set_label_color('transformPivotSP', result_transformPivotSetPieces)
        if not result_transformPivotSetPieces:
            log_message("Transform/Pivot error.")
        
    if pm.checkBox("chk_referenceVersion", query=True, value=True):
        result_referenceVersion = isLatestVersionOfSetPiece()
        set_label_color('referenceVer', result_referenceVersion)
        if not result_referenceVersion:
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
    naming_convention_pattern = re.compile(r'.*v\d{3}.*')
    
    all_valid = True
    excluded_assets = {'persp', 'perspShape', 'top', 'topShape', 'front', 'frontShape', 'side', 'sideShape'}

    for asset in pm.ls(dag=True):
        asset_name = asset.name()
        
        if asset_name in excluded_assets:
            continue

        if not naming_convention_pattern.match(asset_name):
            log_message(f"Asset naming convention error for: {asset_name}")
            all_valid = False
    return all_valid


def isNodeHierarchyValid():
    # Check if geometries are correctly grouped
    for geometry in pm.ls(dag=True, geometry=True):
        parents = geometry.getAllParents()
        if not parents or 'geometry_group' not in parents[0].name().lower():
            log_message(f"Geometry not correctly grouped: {geometry}")
            return False

    # Check if cameras or lights are not parented under geometries
    for node in pm.ls(dag=True, type=['camera', 'light']):
        parents = node.getAllParents()
        if parents and 'geometry' in parents[0].nodeType(inherited=True):
            log_message(f"Invalid parent for {node}: {parents[0]}")
            return False

    # Check for unexpected nodes at the root level
    root_nodes = pm.ls(assemblies=True)
    allowed_root_nodes = ['camera_group', 'lights_group']
    for node in root_nodes:
        if node.name().lower() not in allowed_root_nodes:
            log_message(f"Unexpected root node: {node}")
            return False

    return True

def areReferencesValid():
    all_valid = True

    for ref in pm.listReferences():
        # Check if reference is loaded
        if not ref.isLoaded():
            log_message(f"Reference not loaded: {ref.refNode}")
            all_valid = False

        # Check if reference file still exists
        file_path = ref.path
        if not os.path.exists(file_path):
            log_message(f"Reference file does not exist: {file_path}")
            all_valid = False

        # Check if referenced nodes have errors
        ref_nodes = ref.nodes()
        for node in ref_nodes:
            if pm.hasAttr(node, "hasErrors"):
                if pm.getAttr(f"{node}.hasErrors"):
                    log_message(f"Referenced node has errors: {node}")
                    all_valid = False

    return all_valid

def checkAttributesForNaN():
    all_valid = True
    
    for node in pm.ls(dag=True, type="transform"):
        for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz"]:
            attr_obj = node.attr(attr)  # Get attribute object
            
            # Check if the attribute is not locked and not connected
            if not attr_obj.isLocked() and not attr_obj.isConnected():
                val = attr_obj.get()
                
                # Check for NaN or infinite values
                if math.isnan(val) or math.isinf(val):
                    log_message(f"Invalid attribute value in {node}.{attr}: {val}")
                    attr_obj.set(0)  # Resetting the attribute to zero
                    all_valid = False
                
                # Round very small decimals
                elif abs(val) < 0.0001:
                    attr_obj.set(round(val, 4))
                    
            elif math.isnan(val) or math.isinf(val):
                # Log a message if the attribute is NaN or infinite, but don't try to modify it
                log_message(f"Unable to modify locked or connected attribute with invalid value: {node}.{attr}")
                
    return all_valid


def isCameraApertureValid():
    all_valid = True
    acceptable_aspect_ratios = [16/9.0, 4/3.0]

    for cam_transform in pm.ls(type="transform"):
        # Find all camera shapes under each transform
        cam_shapes = pm.listRelatives(cam_transform, children=True, shapes=True, type='camera')
        
        if not cam_shapes:
            # No camera shapes found, skip it
            continue

        cam_shape = cam_shapes[0]
        camera_name = cam_transform.name()

        # Skip default cameras
        if camera_name in ['persp', 'top', 'front', 'side']:
            continue

        try:
            # Get the aperture attributes
            film_width = cam_shape.getAttr("horizontalFilmAperture")
            film_height = cam_shape.getAttr("verticalFilmAperture")

            # Calculate the aspect ratio
            if film_height != 0:
                aspect_ratio = film_width / film_height

                # Check if the aspect ratio is within the acceptable ratios
                if not any(math.isclose(aspect_ratio, ratio, rel_tol=1e-5) for ratio in acceptable_aspect_ratios):
                    log_message(f"Invalid aspect ratio for camera: {camera_name}")
                    all_valid = False

        except pm.MayaAttributeError as e:
            log_message(f"Error accessing aperture attributes for camera '{camera_name}': {e}")
            all_valid = False

    return all_valid


def isFocalLengthAndFStopValid():
    all_valid = True
    
    valid_focal_lengths = [12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150]
    valid_f_stops = [1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22]
    
    for cam in pm.ls(type="camera"):
        camera_transform = pm.listRelatives(cam, parent=True)[0]  # Get the transform node of the camera
        camera_name = camera_transform.name()
        
        try:
            focal_length = cam.getAttr("focalLength")
            f_stop = cam.getAttr("fStop")
            
            if focal_length not in valid_focal_lengths:
                log_message(f"Invalid focal length for camera {camera_name}: {focal_length}")
                all_valid = False
            
            if f_stop not in valid_f_stops:
                log_message(f"Invalid f-stop for camera {camera_name}: {f_stop}")
                all_valid = False
                
        except pm.MayaAttributeError:
            log_message(f"Attribute error accessing focal length or f-stop for camera: {camera_name}")
            all_valid = False
            
    return all_valid

def isTransformAndPivotAtOrigin():
    all_valid = True
    
    for node in pm.ls(dag=True, type="transform"):
        if "mRef" in node.name():
            # Get the world space coordinates of the rotate pivot
            rotate_pivot = pm.xform(node, query=True, worldSpace=True, rotatePivot=True)
            # Get the world space coordinates of the scale pivot
            scale_pivot = pm.xform(node, query=True, worldSpace=True, scalePivot=True)
            
            translation = node.getTranslation(space="world")
            
            if translation != (0, 0, 0) or rotate_pivot[:3] != (0, 0, 0) or scale_pivot[:3] != (0, 0, 0):
                log_message(f"Invalid transform or pivot for node: {node}")
                all_valid = False
                
    return all_valid

def isLatestVersionOfSetPiece():
    all_valid = True
    
    # Compile the regex pattern outside of the loop for efficiency
    version_pattern = re.compile(r'v(\d+)')
    
    for ref in pm.listReferences():
        file_path = ref.path
        dir_path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        
        # Extract the version number from the file name
        version_match = version_pattern.search(file_name)
        if version_match:
            current_version = int(version_match.group(1))
            highest_version = current_version
            
            # Get all files in the directory
            files_in_directory = os.listdir(dir_path)
            
            # Find the highest version number in the directory
            for other_file in files_in_directory:
                other_version_match = version_pattern.search(other_file)
                if other_version_match:
                    other_version = int(other_version_match.group(1))
                    highest_version = max(highest_version, other_version)
            
            # Check if the current version is not the highest
            if current_version < highest_version:
                log_message(f"Outdated reference: {file_name} (current: v{current_version}, latest: v{highest_version})")
                all_valid = False
    
    return all_valid

main()
