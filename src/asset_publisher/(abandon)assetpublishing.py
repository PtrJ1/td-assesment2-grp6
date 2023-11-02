import maya.cmds as cmds
import os
import sys
from PySide2 import QtWidgets, QtGui
import datetime

# 将UI对象设为全局变量
publish_ui = None

class AssetPublishUI(QtWidgets.QWidget):
    def __init__(self):
        super(AssetPublishUI, self).__init__()
        self.setWindowTitle('Asset Publish')
        self.setGeometry(100, 100, 400, 200)

        self.format_label = QtWidgets.QLabel('File Name Format:')
        self.format_edit = QtWidgets.QLineEdit()
        self.format_edit.setPlaceholderText('Enter file name format...')

        self.location_label = QtWidgets.QLabel('Publish Location:')
        self.location_edit = QtWidgets.QLineEdit()
        self.location_edit.setPlaceholderText('Select publish location...')
        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.browse_location)

        self.publish_button = QtWidgets.QPushButton('Publish')
        self.publish_button.clicked.connect(self.publish_asset)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.format_label)
        layout.addWidget(self.format_edit)
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.publish_button)

        self.setLayout(layout)

        self.selected_objects = []

    def browse_location(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Publish Location')
        if folder:
            self.location_edit.setText(folder)

    def publish_asset(self):
        format_text = self.format_edit.text()
        location_text = self.location_edit.text()

        if not format_text:
            QtWidgets.QMessageBox.critical(self, 'Error', 'File Name Format cannot be empty.')
            return

        if not location_text:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Publish Location cannot be empty.')
            return

        selected_objects = cmds.ls(selection=True, long=True)
        if not selected_objects:
            QtWidgets.QMessageBox.critical(self, 'Error', 'No objects selected for publishing.')
            return

        # 获取当前日期
        current_date = datetime.datetime.now().strftime('%Y%m%d')

        for i, obj in enumerate(selected_objects):
            # 构建文件名
            file_name = f"{obj}_{current_date}_{i+1}"
            file_path = os.path.join(location_text, file_name)

            try:
                cmds.file(rename=file_path)
                cmds.file(save=True, type='mayaBinary')
                QtWidgets.QMessageBox.information(self, 'Success', f'{obj} published to {file_path}')
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to publish {obj}: {str(e)}')

def show_publish_ui():
    global publish_ui
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    
    publish_ui = AssetPublishUI()
    publish_ui.show()

if __name__ == '__main__':
    show_publish_ui()
