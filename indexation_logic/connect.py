import pylocalc


class Connector:

    def __init__(self, path):
        self.path = path

    def conectToDocument(self):
        doc = pylocalc.Document(self.path)
        doc.connect()
        return doc

    def getTableBorder(self):

        return [leftLetter, leftNumber, rightLetter, rightNumber]

def validateBorder(value):
    letter = value[0]
    try:
        number = int(value[1:])
        return number, letter
    except:
        print("Not valid data")
        return "Not valid data"
