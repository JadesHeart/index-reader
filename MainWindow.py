from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget

from indexation_logic.connect import Connector
from indexation_logic.indexing_block import IndexingBlock, wrightComponent


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('untitled.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.generate_button.click.connect(self.fill_indexing_months())

    def fill_indexing_months(self):
        connect = Connector("ukazat.ods")
        indexingBlock = IndexingBlock(connect)
        a, _, b, _ = connect.getTableBorder()
        wright = indexingBlock.count(a, b)
        wrightComponent(wright)
