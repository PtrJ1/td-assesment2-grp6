import maya.cmds as cmds
import os

def create_scene_setup_ui():
    if cmds.window("Setup Window", exists=True):
        cmds.deleteUI("Setup Window")
    
    scene_setup_win = cmds.window("Setup Window", title="Lighting Scene Tool", widthHeight=(500, 400))
    cmds.columnLayout(adjustableColumn=True)

    # Create a text field for file path
    # Insert the folder file path in "/insert/folder/path"
    file_path_field = cmds.textFieldGrp(label="File Path: ", columnWidth=[1, 100], text="/insert/folder/path")
    
    cmds.separator(h=10)
    
    # Create a button to import assets
    cmds.button(label="Import Asset", command=lambda *args: import_assets(file_path_field))
    
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

def import_assets(folder_path_field):
    folder_path = cmds.textFieldGrp(folder_path_field, query=True, text=True)

    if not folder_path:
        cmds.warning("Please specify the folder path.")
        return

    # List files in the specified folder
    file_list = os.listdir(folder_path)
    if not file_list:
        cmds.warning("No files found in the specified folder.")
        return

    try:
        # Import all files from the folder
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                cmds.file(file_path, i=True)
        cmds.warning("Assets imported successfully.")
    except Exception as e:
        cmds.warning("Failed to import assets: " + str(e))
    
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
