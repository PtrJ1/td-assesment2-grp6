import maya.cmds as cmds

def create_scene_setup_ui():
    if cmds.window("Setup Window", exists=True):
        cmds.deleteUI("Setup Window")
    
    scene_setup_win = cmds.window("Setup Window", title="Scene Setup Tool", widthHeight=(300, 200))
    cmds.columnLayout(adjustableColumn=True)

    # Create a text field for file path
    file_path_field = cmds.textFieldGrp(label="FBX File Path: ", columnWidth=[1, 100])
    
    # Create a button to browse and insert the FBX file
    cmds.button(label="Browse and Insert FBX", command=lambda *args: insert_fbx(file_path_field))
    
    cmds.showWindow(scene_setup_win)

def insert_fbx(file_path_field):
    file_path = cmds.textFieldGrp(file_path_field, query=True, text=True)
    
    if not file_path:
        cmds.warning("Please specify an FBX file path.")
        return

    # Create a new locator to represent the FBX file
    fbx_locator = cmds.createNode("locator", name="FBX_Locator")
    
    # Import the FBX file
    try:
        cmds.file(file_path, i=True, type="FBX", rpr="FBX", options="v=0;", pr=True, loadReferenceDepth="all")
    except Exception as e:
        cmds.warning("Failed to insert FBX file: " + str(e))
        return

    # Parent the FBX locator to the imported FBX objects
    imported_fbx_objects = cmds.ls(type="transform", long=True)
    if imported_fbx_objects:
        cmds.parent(fbx_locator, imported_fbx_objects[0])

    cmds.warning("FBX file inserted successfully.")

def run_scene_setup_tool():
    create_scene_setup_ui()

run_scene_setup_tool()
