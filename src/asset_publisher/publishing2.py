import maya.cmds as cmds
import os
import sys
from PySide2 import QtWidgets, QtGui
import datetime
publish_ui = None

class AssetPublishUI(QtWidgets.QWidget):
    def __init__(self):
        super(AssetPublishUI, self).__init__()
        self.setWindowTitle('Asset Publish')
        self.setGeometry(100, 100, 400, 200)

        self.location_label = QtWidgets.QLabel('Publish Location:')
        self.location_edit = QtWidgets.QLineEdit()
        self.location_edit.setPlaceholderText('Select publish location...')
        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_location)

        self.preview_label = QtWidgets.QLabel('Preview:')
        self.preview_text = QtWidgets.QLabel()
        self.preview_text.setWordWrap(True)

        self.publish_button = QtWidgets.QPushButton('Publish')
        self.publish_button.clicked.connect(self.publish_asset)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.preview_label)
        layout.addWidget(self.preview_text)
        layout.addWidget(self.publish_button)

        self.setLayout(layout)

        self.selected_objects = []

    def browse_location(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Publish Location')
        if folder:
            self.location_edit.setText(folder)
            self.update_preview_text()

    def update_preview_text(self):
        location_text = self.location_edit.text()
        if not location_text:
            self.preview_text.setText('')
            return

        selected_objects = cmds.ls(selection=True, long=True)
        if not selected_objects:
            self.preview_text.setText('')
            return

        current_date = datetime.datetime.now().strftime('%Y%m%d')

        preview = "Preview:"
        for obj in selected_objects:
            obj_name = os.path.basename(obj)
            file_path = os.path.join(location_text, f"{obj_name}_{current_date}_vX")
            preview += f"\n{file_path}"

        self.preview_text.setText(preview)

    def publish_asset(self):
        location_text = self.location_edit.text()

        if not location_text:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Publish Location cannot be empty.')
            return

        selected_objects = cmds.ls(selection=True, long=True)
        if not selected_objects:
            QtWidgets.QMessageBox.critical(self, 'Error', 'No objects selected for publishing.')
            return
        current_date = datetime.datetime.now().strftime('%Y%m%d')

        for obj in selected_objects:
            obj_name = os.path.basename(obj)
            file_path = self.get_next_version(location_text, obj_name, current_date)

            try:
                cmds.file(rename=file_path)
                cmds.file(save=True, type='mayaBinary')
                QtWidgets.QMessageBox.information(self, 'Success', f'{obj} published to {file_path}')
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to publish {obj}: {str(e)}')

    def get_next_version(self, location_text, obj_name, current_date):
        version = 1
        while True:
            file_name = f"{obj_name}_{current_date}_v{version}"
            file_path = os.path.join(location_text, file_name)
            if not os.path.exists(file_path):
                return file_path
            version += 1

def show_publish_ui():
    global publish_ui
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    
    publish_ui = AssetPublishUI()
    publish_ui.show()

if __name__ == '__main__':
    show_publish_ui()
