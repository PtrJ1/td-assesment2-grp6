import maya.cmds as cmds 
import os

def export_alembic(output_path):
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No objects selected")
        return
    for obj in selected_objects:
        cmds.select(obj, replace=True
        output_file = output_path + obj + '.abc'
        cmds.AbcExport(j="-frameRange 1 120 -root" + obj + output_file)
         
export_path = "C:/Users/13630811/Documents/maya/projects/default/assets"
export_alembic(export_path)


    
#Animation artist import

def import_alembic(input_path):
    alembic_files = [f for f in os.listdir(input_path)if f.endswith('abc')]
    if not alembic_files:
        cmds.warning("brr")
        
    



