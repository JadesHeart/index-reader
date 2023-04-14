from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QFileDialog

from indexation_logic.connect import Connector
from indexation_logic.indexing_block import IndexingBlock, wrightComponent, stick_month


class MainWindow(QMainWindow):
    combination = ""
    account_file_name = ""
    record_file_name = ""

    def __init__(self):
        super(QMainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.add_one.clicked.connect(self.add_one_number)
        self.add_two.clicked.connect(self.add_two_number)
        self.add_three.clicked.connect(self.add_three_number)
        self.add_four.clicked.connect(self.add_four_number)
        self.generate_button.clicked.connect(self.fill_indexing_months)
        self.generate_quarter.clicked.connect(self.fill_indexing_quarter)
        self.read_file.clicked.connect(self.open_read_file)
        self.record_file.clicked.connect(self.open_record_file)
        self.left_border.mousePressEvent = self.click_on_left_border_input
        self.right_borde.mousePressEvent = self.click_on_right_borde_input
        self.name.mousePressEvent = self.click_on_name_input

    def fill_indexing_months(self):
        connect = Connector(self.account_file_name)
        indexingBlock = IndexingBlock(connect)
        left_border, right_border, categories_location, name = connect.getTableBorder(self)
        wright = indexingBlock.count(left_border, right_border, categories_location, name)
        wrightComponent(wright, self.record_file_name)

    def fill_indexing_quarter(self):
        connect = Connector(self.account_file_name)
        indexingBlock = IndexingBlock(connect)
        left_border, right_border, categories_location, name = connect.getTableBorder(self)
        wright = indexingBlock.count(left_border, right_border, categories_location, name)
        quarter = stick_month(wright)
        wrightComponent(quarter, self.record_file_name)

    def open_read_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Liber Office Calc (*.ods);;Все файлы (*)")
        if filename:
            self.account_file_name = filename

    def open_record_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Liber Office Calc (*.ods);;Все файлы (*)")
        if filename:
            self.record_file_name = filename

    def add_one_number(self):
        self.combination += "1"
        self.categories_location.setText(self.combination)

    def add_two_number(self):
        self.combination += "2"
        self.categories_location.setText(self.combination)

    def add_three_number(self):
        self.combination += "3"
        self.categories_location.setText(self.combination)

    def add_four_number(self):
        self.combination += "4"
        self.categories_location.setText(self.combination)

    def click_on_left_border_input(self, event):
        self.left_border.setText("")

    def click_on_right_borde_input(self, event):
        self.right_borde.setText("")

    def click_on_name_input(self, event):
        self.name.setText("")
