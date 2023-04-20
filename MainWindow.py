from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog

from indexation_logic.indexing_block import IndexingBlock, wrightComponent, stick_month
from time_row_logic.create_time_row import create_time_row


class MainWindow(QMainWindow):
    combination = ""
    combination_time_row = ""
    account_file_name = ""
    record_file_name = ""
    read_time_row_file = ""

    def __init__(self, connect):
        super(QMainWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.connect = connect
        self.add_one.clicked.connect(self.add_one_number)
        self.add_two.clicked.connect(self.add_two_number)
        self.add_three.clicked.connect(self.add_three_number)
        self.add_four.clicked.connect(self.add_four_number)

        self.add_one_3.clicked.connect(self.add_one_number_timerow)
        self.add_two_3.clicked.connect(self.add_two_number_timerow)
        self.add_two_4.clicked.connect(self.add_three_number_timerow)
        self.add_two_5.clicked.connect(self.add_four_number_timerow)

        self.generate_button.clicked.connect(self.fill_indexing_months)
        self.generate_quarter.clicked.connect(self.fill_indexing_quarter)
        self.read_file.clicked.connect(self.open_read_file)
        self.record_file.clicked.connect(self.open_record_file)
        self.left_border.mousePressEvent = self.click_on_left_border_input
        self.right_borde.mousePressEvent = self.click_on_right_borde_input
        self.name.mousePressEvent = self.click_on_name_input
        self.left_border_3.mousePressEvent = self.click_on_left_border_input_timerow
        self.right_borde_3.mousePressEvent = self.click_on_right_borde_input_timerow
        self.name_3.mousePressEvent = self.click_on_name_input_timerow
        self.name_4.mousePressEvent = self.click_on_category_number
        self.name_5.mousePressEvent = self.click_on_quarter_number
        self.time_row_button.clicked.connect(self.fill_time_row_quarter)
        self.read_time_row_file.clicked.connect(self.open_time_row_file)

    def fill_indexing_months(self):
        indexingBlock = IndexingBlock()
        left_border, right_border, categories_location, name = self.connect.getTableBorder(self)
        if self.account_file_name == "":
            return
        connected_doc = self.connect.conectToDocument(self.account_file_name)
        wright = indexingBlock.count(left_border, right_border, categories_location, name, connected_doc)
        print(wright)
        if self.record_file_name == "":
            return
        connected_read_doc = self.connect.conectToDocument(self.record_file_name)
        wrightComponent(wright, connected_read_doc)

    def fill_indexing_quarter(self):
        indexingBlock = IndexingBlock()
        left_border, right_border, categories_location, name = self.connect.getTableBorder(self)
        if self.account_file_name == "":
            return
        connected_doc = self.connect.conectToDocument(self.account_file_name)
        wright = indexingBlock.count(left_border, right_border, categories_location, name, connected_doc)
        if self.record_file_name == "":
            return
        connected_read_doc = self.connect.conectToDocument(self.record_file_name)
        quarter = stick_month(wright)
        create_time_row(quarter, 2, 1)
        wrightComponent(quarter, connected_read_doc)

    def fill_time_row_quarter(self):
        indexingBlock = IndexingBlock()
        left_border, right_border, categories_location, name = self.connect.getTableBorderTimeRow(self)
        if self.open_time_row_file == "":
            return
        connected_doc = self.connect.conectToDocument(self.read_time_row_file)
        wright = indexingBlock.count(left_border, right_border, categories_location, name, connected_doc)
        quarter = stick_month(wright)
        try:
            categories_number = int(self.name_4.text())
            quarter_number = int(self.name_5.text())
        except:
            return
        create_time_row(quarter, categories_number, quarter_number)

    def open_read_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Liber Office Calc (*.ods);;Все файлы (*)")
        if filename:
            self.account_file_name = filename

    def open_record_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Liber Office Calc (*.ods);;Все файлы (*)")
        if filename:
            self.record_file_name = filename

    def open_time_row_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Liber Office Calc (*.ods);;Все файлы (*)")
        if filename:
            self.read_time_row_file = filename

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

    def add_one_number_timerow(self):
        self.combination_time_row += "1"
        self.categories_location_3.setText(self.combination_time_row)

    def add_two_number_timerow(self):
        self.combination_time_row += "2"
        self.categories_location_3.setText(self.combination_time_row)

    def add_three_number_timerow(self):
        self.combination_time_row += "3"
        self.categories_location_3.setText(self.combination_time_row)

    def add_four_number_timerow(self):
        self.combination_time_row += "4"
        self.categories_location_3.setText(self.combination_time_row)

    def click_on_left_border_input(self, event):
        self.left_border.setText("")

    def click_on_right_borde_input(self, event):
        self.right_borde.setText("")

    def click_on_name_input(self, event):
        self.name.setText("")

    def click_on_left_border_input_timerow(self, event):
        self.left_border_3.setText("")

    def click_on_right_borde_input_timerow(self, event):
        self.right_borde_3.setText("")

    def click_on_name_input_timerow(self, event):
        self.name_3.setText("")

    def click_on_category_number(self, event):
        self.name_4.setText("")

    def click_on_quarter_number(self, event):
        self.name_5.setText("")
