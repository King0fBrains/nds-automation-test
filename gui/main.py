"""Entry point for the program"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module

import ctypes
import os
import sys
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow


def main() -> None:
    """Main function to run the Qt Gui and check to see if we're running windows
    and if so, add some logic to display the app icon"""
    app = QApplication(sys.argv)

    if os.name == "nt":
        appid = "NDS Automation.0.0.1"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    icon = QtGui.QIcon('ui//icon.png')
    app.setWindowIcon(icon)
    window = MainWindow()
    window.show()
    window.setWindowIcon(icon)
    app.exec()


if __name__ == "__main__":
    sys.exit(main())
