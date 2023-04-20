import pylocalc
import matplotlib.pyplot as plt


def create_time_row(quarter_list, needed_category, needed_quarter):
    plt.close()
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1920 / dpi, 1080 / dpi))
    plt.xlabel('почтампт')
    plt.ylabel('прибыль в млн руб')
    category_list = []
    pochtamp_list = []
    for i in quarter_list:
        category_list.append(i['parameters'][needed_quarter - 1][needed_category - 1])
        pochtamp_list.append(i['mailPostName'].replace(" ", "\n"))
    print(category_list)
    plt.plot(pochtamp_list, category_list)
    plt.show()
    fig.savefig("category_number" + str(needed_category) + ".png")
