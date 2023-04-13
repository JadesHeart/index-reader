from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget

from indexation_logic.connect import Connector
from indexation_logic.indexing_block import IndexingBlock, wrightComponent


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main.ui', self)# Load the .ui file
        self.show()  # Show the GUI

        self.generate_button.clicked.connect(self.fill_indexing_months)

    def fill_indexing_months(self):
        connect = Connector("ukazat.ods")
        print("GOOOOOOOOOOOOOOOOO")
        indexingBlock = IndexingBlock(connect)
        left_border, right_border, categories_location, last_string = connect.getTableBorder(self)
        wright = indexingBlock.count(left_border, right_border, categories_location, last_string )
        wrightComponent(wright)
