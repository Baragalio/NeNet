import pandas as pd
import random as rnd

header = 'Age;Sex;Color;Season;Activity;Visit_purpose;Number_of_freinds'.split(';')

values = {'Age':[i for i in range(1, 7)],
          'Sex':[1, 2],
          'Color':[i for i in range(1, 8)],
          'Season':[1, 2, 3, 4],
          'Activity': [1, 2, 3],
          'Visit_purpose':[1, 2, 3, 4],
          'Number_of_freinds':[1, 2, 3, 4]}

def generate_activity(age):
    activity = values['Activity']
    x5 = rnd.choice(activity)
    if age in [1, 2]:
        x5 = 1
    elif age == 3:
        x5 = rnd.choice(activity[:2])
    elif age in [4, 5, 6]:
        x5 = rnd.choice(activity[1:])
    return x5

def generate_visit(age, activity):
    visit = values['Visit_purpose']
    x6 = rnd.choice(visit)
    if ((age in [1, 2])|(activity == 6)):
        x6 = rnd.choice([1, 2, 4])
    if ((age in [3, 4, 5, 6])&(activity in [2, 3])):
        x6 = rnd.choice([1, 3, 4])
    return x6


def generate_number(visit):
    number = values['Number_of_freinds']
    if visit == 4:
        x7 = rnd.choice(number[2:])
    else:
        x7 = rnd.choice(number)
    return x7


def data_generate(age, sex, color, season):
    x1 = age
    x2 = sex
    x3 = color
    x4 = season
    x5 = generate_activity(age)
    x6 = generate_visit(age, x5)
    x7 = generate_number(x6)

    return[x1, x2, x3, x4, x5, x6, x7]

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