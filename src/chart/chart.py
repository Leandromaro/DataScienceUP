import matplotlib.pyplot as plt
import os
import pandas as pd

dirname = os.path.dirname(__file__)
COUNTRIES_PERCENTAGE_GROUP_PATH = os.path.join(dirname, '../res/group/countries_percentage.csv')


def pie_chart():
    df = pd.read_csv(COUNTRIES_PERCENTAGE_GROUP_PATH, low_memory=False)
    labels = df.Region
    sizes = df.Percentage
    explode = (0, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('countries_cake.png')
    plt.show()


pie_chart()
