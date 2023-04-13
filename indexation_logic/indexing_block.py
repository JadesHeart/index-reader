import pylocalc

import indexation_logic.connect


class IndexingBlock:

    def __init__(self, connect):
        self.connect = connect

    def count(self, leftLetter, rightLetter, user_input, last_string):
        print("jopa?")
        doc = self.connect.conectToDocument()
        print("jopa?1")
        last_string = int(last_string)
        print(last_string)
        currentMail = "B5"
        numberString = int(currentMail[1:])
        sheet = doc.get_sheet(0)
        cvrtl = findBorder(leftLetter[0], rightLetter[0])
        bdr_list = []
        print("jopa?3")
        user_input.replace(" ", "")
        for i in user_input:
            bdr_list.append(int(i))
        bdr_list = [2, 2, 1, 1, 1, 2, 1, 2]

        mailComponent = {
            "mailPostName": "",
            "parameters": [[]],
        }
        print("jopa?4")
        all_components = []
        mouth = 0
        while numberString < last_string:
            print("jopa?1")
            mouth += 1
            print("Mouth now: " + str(mouth))
            print()
            print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
            oneComponentParam = []
            for i in bdr_list:
                summ = 0
                for j in range(i):
                    summ += int(sheet[cvrtl[mouth - 1] + str(j + numberString)].value.strip().replace(",", ""))
                print("Summ: " + str(summ))
                print(numberString)
                numberString += i
                oneComponentParam.append(summ)
            numberString -= sum(bdr_list)
            print("Component: " + str(oneComponentParam))
            mailComponent["parameters"].append(oneComponentParam)
            if mouth > len(cvrtl) - 1:
                mailComponent["mailPostName"] = sheet[currentMail[0] + str(numberString)].value
                mailComponent["parameters"].pop(0)
                all_components.append(mailComponent)
                mailComponent = {"mailPostName": "",
                                 "parameters": [[]], }
                mouth = 0
                numberString += sum(bdr_list)
        doc.close()
        return all_components


def wrightComponent(all_components):
    doc = pylocalc.Document('eleventest.ods')
    doc.connect()
    sheet = doc[0]
    row = 0
    column = 0
    for i in all_components:
        sheet[column, row].value = i["mailPostName"]
        for j in i["parameters"]:
            print("List of component: " + str(j))
            for z in j:
                column += 1
                sheet[column, row].value = z
            column -= len(j)
            row += 1
        print(i["mailPostName"])
    doc.save()


def findBorder(leftLetter, rightLetter):
    cvrtl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(cvrtl)):
        if cvrtl[i] == leftLetter:
            cvrtl = cvrtl[i:]
            break

    for i in range(len(cvrtl)):
        if cvrtl[i] == rightLetter:
            cvrtl = cvrtl[:i + 1]
            break
    return cvrtl
