import pandas as pd
import random as rnd


pd.set_option('display.max_columns', None)

header = 'Age;Sex;Color;Season;Activity;Visit_purpose;Number_of_purchasses;help_button;search_button;account_button;\
         settings_button;bascket;theme;rgb;font;functional'.split(';')

values = {'Age':[i for i in range(0, 6)],
          'Sex':[0, 1],
          'Color':[i for i in range(0, 7)],
          'Season':[0, 1, 2, 3],
          'Activity': [0, 1, 2],
          'Visit_purpose':[0, 1, 2, 3],
          'Number_of_purchasses':[0, 1, 2, 3],
          'help_button':[0, 1],
          'search_button':[0, 1],
          'account_button':[0, 1],
          'settings_button':[0, 1],
          'bascket': [0, 1],
          'theme':[0, 1],
          'rgb':[0, 1, 2],
          'font':[0, 1, 2, 3],
          'functional':[0, 1, 2]}

def generate_activity(age):
    activity = values['Activity']
    x5 = rnd.choice(activity)
    if age in [0, 1]:
        x5 = 0
    elif age == 2:
        x5 = rnd.choice(activity[:2])
    elif age in [3, 4, 5]:
        x5 = rnd.choice(activity[1:])
    return x5

def generate_visit(age, activity):
    visit = values['Visit_purpose']
    x6 = rnd.choice(visit)
    if ((age in [0, 1])|(activity == 5)):
        x6 = rnd.choice([0, 1, 3])
    if ((age in [2, 3, 4, 5])&(activity in [1, 2])):
        x6 = rnd.choice([0, 2, 3])
    return x6


def generate_number(visit):
    number = values['Number_of_purchasses']
    if visit == 3:
        x7 = rnd.choice(number[2:])
    else:
        x7 = rnd.choice(number)
    return x7


def help_button(age):
    if (age < 3):
        y1 = 0
    else:
        y1 = 1
    return y1


def search_button(age):
    if (age == 2):
        y2 = 0
    else:
        y2 = 1
    return y2


def account_button(age):
    if (age < 4):
        y3 = 0
    else:
        y3 = 1
    return y3


def settings_button(activity):
    if (activity == 3):
        y4 = 1
    else:
        y4 = 0
    return y4


def bascket(purchasses):
    if (purchasses > 2):
        y5 = 0
    else:
        y5 = rnd.choice([0, 1])
    return y5


def theme():
    y6 = rnd.choice(values['theme'])
    return y6


def rgb(color):
    if (color == 0 or color == 1 or color == 2):
        y7 = 1
    elif (color == 3):
        y7 = 2
    else:
        y7 = 0
    return y7


def font(age):
    if (age == 0 or age == 5):
        y8 = 3
    else:
        y8 = rnd.choice(values['font'])
    return y8


def functional(activity, purchasses):
    if (purchasses > 1):
        y9 = 2
    elif (activity == 1):
        y9 = 1
    else:
        y9 = rnd.choice(values['functional'])
    return y9

def data_generate(age, sex, color, season):
    x1 = age
    x2 = sex
    x3 = color
    x4 = season
    x5 = generate_activity(age)
    x6 = generate_visit(age, x5)
    x7 = generate_number(x6)
    y1 = help_button(x1)
    y2 = search_button(x1)
    y3 = account_button(x1)
    y4 = settings_button(x5)
    y5 = bascket(x7)
    y6 = theme()
    y7 = rgb(x3)
    y8 = font(x1)
    y9 = functional(x5, x7)

    return[x1, x2, x3, x4, x5, x6, x7, y1, y2, y3, y4, y5, y6, y7, y8, y9]

data = []
for i in range(20000):
    age = rnd.choice(values['Age'])
    sex = rnd.choice(values['Sex'])
    color = rnd.choice(values['Color'])
    season = rnd.choice(values['Season'])
    data.append(data_generate(age, sex, color, season))

rnd.shuffle(data)
base = pd.DataFrame(data, columns=header)
base.to_csv('database.csv')

print(base.head(10))


