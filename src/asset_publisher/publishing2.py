import maya.cmds as cmds
import os
import sys
from PySide2 import QtWidgets, QtGui
import datetime

# 将UI对象设为全局变量
publish_ui = None
type = 'transform'
class AssetPublishUI(QtWidgets.QWidget):
    def __init__(self):
        super(AssetPublishUI, self).__init__()
        self.setWindowTitle('Asset Publish Tool')
        self.setGeometry(100, 100, 400, 200)

        # Widgets for UI elements
        self.location_label = QtWidgets.QLabel('Project Location:')
        self.location_edit = QtWidgets.QLineEdit()
        self.location_edit.setPlaceholderText('Select project location...')
        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_location)

        self.preview_label = QtWidgets.QLabel('')
        self.preview_text = QtWidgets.QLabel()
        self.preview_text.setWordWrap(True)

        self.publish_button = QtWidgets.QPushButton('Publish')
        self.publish_button.clicked.connect(self.publish_asset)

        # Layout setup
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.preview_label)
        layout.addWidget(self.preview_text)
        layout.addWidget(self.publish_button)

        self.setLayout(layout)

        self.selected_objects = []

    # Browse for the publish location
    def browse_location(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Publish Location')
        if folder:
            # Set the publish location to /publish/assets/props inside the selected folder
            project_location = os.path.join(folder)
            publish_location = os.path.join(folder, 'publish', 'assets', 'props')
            self.location_edit.setText(project_location)
            self.update_preview_text()

    # Update the preview text with generated file names
    def update_preview_text(self):
        location_text = self.location_edit.text()
        if not location_text:
            self.preview_text.setText('')
            return

        selected_objects = cmds.ls(selection=True, long=True)
        if not selected_objects:
            self.preview_text.setText('')
            return

        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y%m%d')

        preview = "Preview:"
        for obj in selected_objects:
            obj_name = os.path.basename(obj)
            publish_location = os.path.join(location_text, 'publis', 'assets', 'props')
            file_path = self.get_next_version(publish_location, obj_name, current_date)
            preview += f"\n{file_path}"

        self.preview_text.setText(preview)

    # Publish the selected assets
    def publish_asset(self):
        location_text = self.location_edit.text()

        if not location_text:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Publish Location cannot be empty.')
            return

        selected_objects = cmds.ls(selection=True, long=True)
        if not selected_objects:
            QtWidgets.QMessageBox.critical(self, 'Error', 'No objects selected for publishing.')
            return

        # Get the current date
        current_date = datetime.datetime.now().strftime('%Y%m%d')

        for obj in selected_objects:
            obj_name = os.path.basename(obj)
            file_path = self.get_next_version(location_text, obj_name, current_date)
            
            try:
                # Determine the file type based on the object type
                object_type = cmds.objectType(obj)
                file_type = None
                
                # Check the object type and set the appropriate file type
                if object_type == 'transform':
                        file_type = 'mayaBinary'  # Model: setPiece or sets
                elif object_type == 'cacheFile':
                    if 'character' in obj_name or 'prop' in obj_name:
                        file_type = 'cache'  # Animation: character/prop animation cache
                
                if file_type:
                    # Export the object with the appropriate file type
                    cmds.file(file_path, exportSelected=True, type=file_type, force=True)
                    QtWidgets.QMessageBox.information(self, 'Success', f'{obj} published to {file_path}')
                else:
                    QtWidgets.QMessageBox.critical(self, 'Error', f'Unsupported object type for {obj}: {object_type}')
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to publish {obj}: {str(e)}')


    # Get the next version with a leading zero (e.g., v001, v002, v003)
    def get_next_version(self, location_text, obj_name, current_date):
        obj_name = obj_name.replace('|', '_')
        version = 1
        while True:
            # Use string formatting to ensure the version number is always three digits (e.g., v001, v002, v003)
            file_name = f"{obj_name}_{current_date}_v{version:03d}"
            file_path = os.path.join(location_text, file_name)
            if not os.path.exists(file_path):
                return file_path

            version += 1

# Show the Asset Publish UI
def show_publish_ui():
    global publish_ui
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    
    publish_ui = AssetPublishUI()
    publish_ui.show()

if __name__ == '__main__':
    show_publish_ui()
    
