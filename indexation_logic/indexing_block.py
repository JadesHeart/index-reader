import pylocalc


class IndexingBlock:

    def count(self, leftLetter, rightLetter, user_input, name, connected_doc):
        doc = connected_doc
        last_string = int(rightLetter[1:])
        currentMail = name
        numberString = int(currentMail[1:])
        sheet = doc.get_sheet(0)
        cvrtl = findBorder(leftLetter[0], rightLetter[0])
        bdr_list = []
        user_input.replace(" ", "")
        for i in user_input:
            bdr_list.append(int(i))
        # bdr_list = [2, 2, 1, 1, 1, 2, 1, 2]

        mailComponent = {
            "mailPostName": "",
            "parameters": [[]],
        }
        all_components = []
        mouth = 0
        while numberString < last_string:
            mouth += 1
            oneComponentParam = []
            for i in bdr_list:
                summ = 0
                for j in range(i):
                    try:
                        summ += int(sheet[cvrtl[mouth - 1] + str(j + numberString)].value.strip().replace(",", ""))
                    except:
                        summ += 0

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
        print("you sosalkaaaaaaa")
        connected_doc.close()
        return all_components


def wrightComponent(all_components, doc):
    try:
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
        doc.close()
    except:
        doc.close()
        print("Can't open document")


def stick_month(all_components):
    itogo = []
    absolute = []
    for j in range(len(all_components)):
        for i in range(len(all_components[j]['parameters'])):  # vse kategori v yanvare
            if (i + 3) == (len(all_components[j]['parameters'])):
                a = all_components[j]['parameters'][i]
                b = all_components[j]['parameters'][i + 1]
                c = all_components[j]['parameters'][i + 2]
                itogo.append(list(map(sum, zip(a, b, c))))
                break
            if (i == 0) | (i % 3 == 0):
                a = all_components[j]['parameters'][i]
                b = all_components[j]['parameters'][i + 1]
                c = all_components[j]['parameters'][i + 2]
                itogo.append(list(map(sum, zip(a, b, c))))
        appended = {
            "mailPostName": all_components[j]['mailPostName'],
            'parameters': itogo
        }
        absolute.append(appended)
        itogo = []
    return absolute


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
