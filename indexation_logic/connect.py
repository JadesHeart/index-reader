import pylocalc


class Connector:

    def __init__(self, path):
        self.path = path

    def conectToDocument(self):
        doc = pylocalc.Document(self.path)
        doc.connect()
        return doc

    def getTableBorder(self, self1):
        try:
            left_border = self1.left_border.text()
            right_border = self1.right_borde.text()
            categories_location = self1.categories_location.text()
            name = self1.name.text()
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
