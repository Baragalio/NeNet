import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD , Adam
from keras.models import load_model
from keras.utils import np_utils

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


NB_EPOCH = 10 # тестить(частота обучения на тестовом наборе)
BATCH_SIZE = 10 # тестить(частота обновления весов)
VERBOSE = 1 # модель вывода(не трогать)
NB_CLASSES = 8 # кол-во выходов
OPTIMIZATOR = Adam() # 'adam' или другой оптимизатор
VALIDATION_SPLIT = 0.2 # % контрольного набора
DROPOUT = 0.1 # Прореживание
INPUT_ITOG = 9 # Вписать размер выхода

df = pd.read_csv('database.csv', index_col=0)

df = df.drop(['id'], axis=1)
labels = df.columns
x = df[labels[:7]] # Данные
y = df[labels[7:]] # Целевая переменная
X = []
x = np.array(x)
x = x.tolist()

Y = []
y = np.array(y)

userid = 0
while userid != 20000:
	temp = prediction(x[userid])
	X.append(temp[0])
	userid += 1

X = np.array(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model = Sequential()
model.add(Dense(256, activation = 'relu' ,input_shape = (X_train.shape[1],)))
model.add(Dropout(DROPOUT))
model.add(Dense(512, activation = 'relu'))
model.add(Dense(256, activation = 'relu'))
model.add(Dense(INPUT_ITOG, activation = 'hard_sigmoid')) #0 если X < -2.5, 1 если x > 2.5, 0.2*x+0.5 если -2.5 <=x<= 2.5
model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = OPTIMIZATOR, metrics = ['accuracy'])
#обучение
model.fit(X_train, y_train, batch_size = BATCH_SIZE, epochs = NB_EPOCH, verbose = VERBOSE, validation_split = 0.2)
#оценка точности
loss, accuracy = model.evaluate(X_test, y_test, verbose = VERBOSE)
print('total loss: {} , total accuracy: {}'.format(loss,  accuracy))

model.save('model2.h5')

