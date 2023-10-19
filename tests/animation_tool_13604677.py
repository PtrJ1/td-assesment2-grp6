import os
from maya import cmds

root_folder = "/tmp/week5"

def Import():
    if os.path.isdir(root_folder):
        for asset_type in os.listdir(root_folder):
            for asset in os.listdir(os.path.join(root_folder,asset_type)):
                latest = root_folder + "/" + asset_type + "/" + asset + "/{0}_layout_v{1}.abc".format(asset, str(GetLatestVersionNumber(asset, asset_type)).zfill(3))

                alembic_options = ";readAnimData=1;useAsAnimationCache=1"
                ns = asset + "NS"
                if not cmds.ls("|{0}|{1}".format(asset_type,ns + ":" + asset)):
                    
                    ref = cmds.file(
                        latest,
                        reference=True,
                        options=alembic_options,
                        lockReference=False,
                        loadReferenceDepth="all",
                        namespace=ns,
                        returnNewNodes=False
                    )
                    
                    if(not cmds.objExists("|"+asset_type)):
                        cmds.createNode('transform', name=asset_type)
                
                    cmds.parent(ns + ":" + asset, asset_type)

def Export():
    asset_types_to_export = ["characters", "props"]
    
    for asset_type in asset_types_to_export:
        asset_group = "|" + asset_type
        if cmds.objExists(asset_group):
            asset_roots = cmds.listRelatives(asset_group, children=True, fullPath=True)

            for asset in asset_roots:
                asset_name = asset.split("|")[-1]
                export_dir = "{0}/{1}/{2}".format(root_folder,asset_type,asset_name)
                try:
                    os.makedirs(export_dir)
                except OSError:
                    print(export_dir + " already exists")
                file_name = "{0}_layout_v{1}.abc".format(asset_name, str(GetNextVersionNumber(asset_name, asset_type)).zfill(3))
                export_file = export_dir + "/" + file_name
                alembic_args = [
                    '-renderableOnly',
                    '-file ' + export_file,
                    '-uvWrite',
                    '-writeFaceSets',
                    '-worldSpace',
                    '-writeVisibility',
                    '-dataFormat ogawa',
                    '-root ' + asset,
                    '-fr %d %d' % (cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
                ]
                print(alembic_args)
                cmds.AbcExport(j = " ".join(alembic_args))

def GetLatestVersionNumber(asset_name, asset_type):
    dir = "{0}/{1}/{2}".format(root_folder,asset_type,asset_name)
    found = False
    count = 1
    while found == False:
        if not os.path.isfile(dir + "/{0}_layout_v{1}.abc".format(asset_name, str(count).zfill(3))):
            found = True
            count = count - 1
        else:
            count = count + 1
    return count

def GetNextVersionNumber(asset_name, asset_type):
    return GetLatestVersionNumber(asset_name, asset_type) + 1
    
Import()

class Window(object):
        
    def __init__(self):
            
        self.window = "Window"
        self.title = "Import/Export"
        self.size = (200, 100)
            
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout(adjustableColumn = True)

        cmds.button(label='Import')
        cmds.button(label='Export')
        
        cmds.showWindow()

                                   
myWindow = Window()