
import numpy as np
import _sqlite3 as sql
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, hard_sigmoid
from keras.util import np_utils  # to_categorical
# импортируем Данные

NB_EPOCH = 10 #тестить(частота обучения на тестовом наборе)
BATCH_SIZE = 1 #тестить(частота обновления весов)
VERBOSE = 2 # модель вывода(не трогать)
NB_CLASSES = 7# кол-во выходов
OPTIMIZATOR = SGD() # или другой оптимизатор
VALIDATION_SPLIT = 0.2 # % контрольного набора
DROPOUT = 0.05 #Прореживание
INPUT_ITOG = 9 # Вписать размер выхода
Mas_x[[]]
Mas_y[[]]

#загурзка данных из mysql для работы
sql_table = sql.connect('name_table') #название таблицы
cursor = sql_table.cursor()
userid = 0
while userid != 5:
	userid += 1
	crsr.execute('SELECT colimns_of_answers from name_table WHERE id ='  + userid)# подставить название таблицы и столбцов ответов
	Mas_x.append(crcr.fetchall())
INPUT = len(Mas_x)
X_train = Mas_x[range(0,8)]
X_test =  Mas_x[range(8,10)]
userid = 0
while userid != 5:
	userid += 1
	crsr.execute('SELECT colimns_of_blocks from name_table WHERE id ='  + userid)# подставить название таблице и столбцов блоков
	Mas_y.append(crcr.fetchall())

Y_train = Mas_y[range(0,8)]
Y_test = Mas_y[range(8,10)]

X_train = X_train.reshape(len(X_train), 7)
X_test = X_test.reshape(len(X_test), 7)

X_train = X_train.astype('float32') # уточнить нужный тип
X_test = X_test.astype('float32')

Y_train = np_utils.to_categorical(Y_train, NB_CLASSES) #точная библиотека
Y_test = np_utils.to_categorical(Y_test, NB_CLASSES)

#Core
model = Sequential() # пропробовать разные модели
model.add(Dense(NB_CLASSES, activation = 'relu' ,input_shape = (INPUT,)))
model.add(Dropout(DROPOUT))
model.add(Dense(NB_CLASSES, activation = 'relu'))
model.add(Dense(INPUT_ITOG, activation = 'hard_sigmoid')) #0 если X < -2.5, 1 если x > 2.5, 0.2*x+0.5 если -2.5 <=x<= 2.5
model.summary()

#компиляция
model.complite(loss = 'mean_squared_error', optimizer = OPTIMIZATOR, metrics = ['accuracy'])
#старая функция потерь - categorical_crossentropy

#обучение
history = model.fit(X_train, Y_train, batch_size = BATCH_SIZE, epochs = NB_EPOCH, verbose = VERBOSE, validation_split = VALIDATION_SPLIT)

#Оценка точности
accuracy = model.evaluate(X_test, Y_test, verbose = VERBOSE)
print('Точность:', accuracy[1])

model.save('model.h5')

#прогноз из бд
sql_table = sql.connect('name_table_registration')
userid =
crsr.execute('SELECT colimns_of_answers from name_table WHERE id ='  + userid)
registration_data = crcr.fetchall()
output = model.predict(registration_data)