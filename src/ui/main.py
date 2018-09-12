from ui import application

import sys
from PySide2 import QtWidgets


from ui.auto import main_window_ui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()

    def setupUI(self):
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    main_window = MainWindow()
    main_window.show()
    sys.exit(QtWidgets.QApplication.exec_())