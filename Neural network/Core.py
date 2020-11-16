import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD , Adam
from keras.models import load_model
from keras.utils import np_utils

# импортируем Данные
def prediction(registration_data):
	registration_data[0] = np_utils.to_categorical(registration_data[0], 6, dtype='int')
	registration_data[1] = np_utils.to_categorical(registration_data[1], 2, dtype='int')
	registration_data[2] = np_utils.to_categorical(registration_data[2], 7, dtype='int')
	registration_data[3] = np_utils.to_categorical(registration_data[3], 4, dtype='int')
	registration_data[4] = np_utils.to_categorical(registration_data[4], 3, dtype='int')
	registration_data[5] = np_utils.to_categorical(registration_data[5], 4, dtype='int')
	registration_data[6] = np_utils.to_categorical(registration_data[6], 4, dtype='int')
	reg_data_2 = []
	for j in registration_data:
		for i in j:
			reg_data_2.append(i)
	reg_data_2 = np.array([reg_data_2])
	return reg_data_2

NB_EPOCH = 10 #тестить(частота обучения на тестовом наборе)
BATCH_SIZE = 1 #тестить(частота обновления весов)
VERBOSE = 1 # модель вывода(не трогать)
NB_CLASSES = 8# кол-во выходов
OPTIMIZATOR = Adam() # 'adam' или другой оптимизатор
VALIDATION_SPLIT = 0.2 # % контрольного набора
DROPOUT = 0.05 #Прореживание
INPUT_ITOG = 9 # Вписать размер выхода
Mas_x = []
Mas_y = []

#загурзка данных для работы
df = pd.read_csv('database.csv')
userid = 0
j = df['Age;Sex;Color;Season;Activity;Visit_purpose;Number_of_purchasses'.split(';')]
t_x = []
while userid != 20000:
	temp = j.iloc[userid].values
	t_x.append(temp)
	userid += 1
userid = 0

t_x = np.array(t_x, int)
t_x = t_x.tolist()

while userid != 20000:
	d = prediction(t_x[userid])
	Mas_x.append(d[0])
	userid += 1
Mas_x = np.array(Mas_x, float)

j = df['help_button;search_button;account_button;settings_button;bascket;theme;rgb;font;functional'.split(';')]
t_y = []
userid = 0
while userid != 20000:
	temp = j.iloc[userid].values
	t_y.append(temp)
	userid += 1
userid = 0

t_y = np.array(t_y, int)
t_y = t_y.tolist()

while userid != 20000:
	Mas_y.append(t_y[userid])
	userid += 1
Mas_y = np.array(Mas_y, float)

X_train = Mas_x
# #X_train = X_train.astype('float32')
Y_train = Mas_y
print(X_train.shape[1] )

#Core
model = Sequential() # пропробовать разные модели
model.add(Dense(NB_CLASSES, activation = 'relu' ,input_shape = (X_train.shape[1],)))
model.add(Dropout(DROPOUT))
model.add(Dense(NB_CLASSES, activation = 'relu'))
model.add(Dense(NB_CLASSES, activation = 'relu'))
model.add(Dense(INPUT_ITOG, activation = 'hard_sigmoid')) #0 если X < -2.5, 1 если x > 2.5, 0.2*x+0.5 если -2.5 <=x<= 2.5
model.summary()

#компиляция
model.compile(loss = 'mean_squared_error', optimizer = OPTIMIZATOR, metrics = ['accuracy'])
#старая функция потерь - categorical_crossentropy

#обучение
model.fit(X_train, Y_train, batch_size = BATCH_SIZE, epochs = NB_EPOCH, verbose = VERBOSE, validation_split = VALIDATION_SPLIT)

#Оценка точности
#accuracy = model.evaluate(X_test, Y_test, verbose = VERBOSE)
#print('Точность:', accuracy[1])

#model.save('model.h5')

#прогноз из бд
#sql_table = sql.connect('name_table_registration')
#userid = 1
#crsr.execute('SELECT colimns_of_answers from name_table WHERE id ='  + userid)
#registration_data = crcr.fetchall()
#output = model.predict(registration_data)