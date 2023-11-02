import maya.cmds as cmds

def create_scene_setup_ui():
    if cmds.window("Setup Window", exists=True):
        cmds.deleteUI("Setup Window")
    
    scene_setup_win = cmds.window("Setup Window", title="Lighting Scene Tool", widthHeight=(500, 400))
    cmds.columnLayout(adjustableColumn=True)

    # Create a text field for file path
    file_path_field = cmds.textFieldGrp(label="Asset File Path: ", columnWidth=[1, 100])
    
    cmds.separator(h=10)
    
    # Create a button to browse and insert the FBX file
    cmds.button(label="Browse and Insert Asset", command=lambda *args: insert_fbx(file_path_field))
    
    cmds.separator(h=10)
    
    # Create the first combo box
    character_combo = cmds.optionMenu(label="Character:")
    # Add items to the combo box as needed
    cmds.menuItem(label="Character 1")
    cmds.menuItem(label="Character 2")
    
    cmds.separator(h=10)

    # Create the second combo box
    prop_combo = cmds.optionMenu(label="Prop:")
    # Add items to the combo box as needed
    cmds.menuItem(label="Prop 1")
    cmds.menuItem(label="Prop 2")
    
    cmds.separator(h=10)

    # Create the third combo box
    prop_combo = cmds.optionMenu(label="Camera:")
    # Add items to the combo box as needed
    cmds.menuItem(label="Camera 1")
    cmds.menuItem(label="Camera 2")
    
    cmds.separator(h=10)
    
    # Create 'Import Character' button
    cmds.button(label="Import Character", command=lambda *args: import_selected("Character"))
    
    cmds.separator(h=10)

    # Create 'Import Prop' button
    cmds.button(label="Import Prop", command=lambda *args: import_selected("Prop"))
    
    cmds.separator(h=10)

    # Create 'Import Camera' button
    cmds.button(label="Import Camera", command=lambda *args: import_selected("Camera"))
    
    cmds.separator(h=10)
    
    cmds.button(label="Check Version")
    
    cmds.separator(h=10)
    
    cmds.button(label="Update Version")
    
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
    
def isLatestVersionOfSetPiece():
    all_valid = True
    
    for ref in pm.listReferences():
        file_path = ref.path
        dir_path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        
        # Extract the version number from the file name
        version_match = re.search(r'v(\d+)', file_name)
        if version_match:
            current_version = int(version_match.group(1))
            
            # Get all files in the dir
            files_in_directory = os.listdir(dir_path)
            
            # Check if there's a higher version in the dir
            for other_file in files_in_directory:
                other_version_match = re.search(r'v(\d+)', other_file)
                if other_version_match:
                    other_version = int(other_version_match.group(1))
                    if other_version > current_version:
                        log_message(f"Outdated reference: {file_name}")
                        all_valid = False
                        break  # Break once an outdated reference is found
    
    return all_valid

def run_scene_setup_tool():
    create_scene_setup_ui()

run_scene_setup_tool()