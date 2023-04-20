from MainWindow import MainWindow
import sys
from PyQt6.QtWidgets import QApplication

from indexation_logic.connect import Connector

if __name__ == '__main__':
    app = QApplication(sys.argv)
    connect = Connector()
    mainWindow = MainWindow(connect)
    sys.exit(app.exec())
