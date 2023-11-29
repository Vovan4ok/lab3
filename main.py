import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


number_of_translators = 1
speed = 2
cost = 10
hours = 8
days = 5
bad_feel_possibility = 0.05
math_hope_pages_per_doc = 7
modeling_durability = 60
earned_money_per_every_day = []
lost_money_per_every_day = []
translated_pages_per_every_day = []
max_pages = speed * hours * number_of_translators
burnt_pages_per_every_day = []
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
speed_per_every_day = []


def get_docs_number_for_the_day(day):
    docs_number = 0
    if day == "monday":
        docs_number = np.random.randint(2, 4)
    elif day == "tuesday":
        docs_number = np.random.randint(2, 6)
    elif day == "wednesday":
        docs_number = np.random.randint(3, 8)
    elif day == "thursday":
        docs_number = np.random.randint(2, 5)
    else:
        docs_number = np.random.randint(1, 3)
    return docs_number


def model_immitation():
    for i in range(modeling_durability):
        day = days_of_week[i % 5]
        docs_number = get_docs_number_for_the_day(day)
        total_pages_for_this_day = 0

        if np.random.rand() >= bad_feel_possibility:
            total_pages_for_this_day = docs_number * np.random.poisson(math_hope_pages_per_doc)

        if total_pages_for_this_day < max_pages:
            translated_pages_for_this_day = total_pages_for_this_day
            burnt_pages_per_every_day.append(0)
        else:
            translated_pages_for_this_day = max_pages
            burnt_pages_per_every_day.append(total_pages_for_this_day - translated_pages_for_this_day)

        translated_pages_per_every_day.append(translated_pages_for_this_day)
        earned_money_per_every_day.append(translated_pages_per_every_day[i] * cost)
        lost_money_per_every_day.append(burnt_pages_per_every_day[i] * cost)
        speed_per_every_day.append(translated_pages_per_every_day[i] / hours)

        print("####################################################################################################################")
        print("Номер ітерації: " + str(i))
        print("День тижня: " + day)
        print("Кількість документів, які надйшли на переклад: " + str(docs_number))
        print("Загальна кількість сторінок: " + str(total_pages_for_this_day))
        print("Кількість сторінок, які зміг перекласти перекладач відповідно до свєї максимальної шквидкості: " + str(translated_pages_per_every_day[i]))
        print("Було принесено коштів компанії за поточний день: " + str(earned_money_per_every_day[i]))
        print("Кількість сторінок, яка 'згоріла' через те, що швидкість перекладача обмежена: " + str(burnt_pages_per_every_day[i]))
        print("Було втрачено коштів компанією за поточний день: " + str(lost_money_per_every_day[i]))
        print("Швидкість перекладача за день (сторінок в годину): " + str(speed_per_every_day[i]))
        print("####################################################################################################################")


def build_histogramma():
    plt.figure(figsize=(13, 5))
    plt.bar(list(range(0, modeling_durability)), translated_pages_per_every_day, color="green", label="Перекладені")
    plt.bar(list(range(0, modeling_durability)), burnt_pages_per_every_day, color="red", label="Згоріли")
    plt.xlabel("Ітерація")
    plt.ylabel("Сторінок")
    plt.ylim((0, 20))
    plt.title("Гістограма співвідношення кількості сторінок по дням")
    plt.legend(loc="upper right")
    plt.show()


def build_table():
    table = {"Зароблено коштів": earned_money_per_every_day,
             "Втрачено коштів": lost_money_per_every_day}
    table = pd.DataFrame(table, index=[i for i in range(modeling_durability)])
    print(table)


def build_graphic():
    sum = 0
    for i in range(len(translated_pages_per_every_day)):
        sum += translated_pages_per_every_day[i]
    average_pages = sum / modeling_durability
    average_pages_arr = [average_pages for i in range(modeling_durability)]
    plt.figure(figsize=(15, 5))
    plt.plot([i for i in range(modeling_durability)], translated_pages_per_every_day, label="Кількість сторінок")
    plt.plot([i for i in range(modeling_durability)], average_pages_arr, label="Середня кількість сторінок", color="red")
    plt.xlabel("№ дня")
    plt.ylabel("Кількість сторінок")
    plt.title("Загруженість перекладача по дням")
    plt.legend(loc="upper right")
    plt.show()

def main():
    model_immitation()
    build_histogramma()
    build_table()
    build_graphic()


main()
