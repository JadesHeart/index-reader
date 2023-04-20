import time

import pylocalc


class Connector:

    def conectToDocument(self, path):
        doc = pylocalc.Document(path)
        while True:
            try:
                doc.connect()
                return doc
            except ConnectionError:
                time.sleep(5)

    def getTableBorder(self, self1):
        try:
            left_border = self1.left_border.text()
            right_border = self1.right_borde.text()
            categories_location = self1.categories_location.text()
            name = self1.name.text()
        except:
            print("Fuuuuck")
        return left_border, right_border, categories_location, name
    def getTableBorderTimeRow(self, self1):
        try:
            left_border = self1.left_border_3.text()
            right_border = self1.right_borde_3.text()
            categories_location = self1.categories_location_3.text()
            name = self1.name_3.text()
        except:
            print("Fuuuuck")
        return left_border, right_border, categories_location, name


def validateBorder(value):
    letter = value[0]
    try:
        number = int(value[1:])
        return number, letter
    except:
        print("Not valid data")
        return "Not valid data"
