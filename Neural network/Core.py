
import numpy as np
import _sqlite3 as sql
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
# импортируем Данные

NB_EPOCH = 1 #тестить(частота обучения на тестовом наборе)
BATCH_SIZE = 1 #тестить(частота обновления весов)
VERBOSE = 2 # модель вывода(не трогать)
NB_CLASSES = 1# кол-во выходов
OPTIMIZATOR = SGD() # или другой оптимизатор
VALIDATION_SPLIT = 0.2 # % контрольного набора
DROPOUT = 0.2 #Прореживание
INPUT = 10 # Вписать размер вектор векторов
Mas_x[[]]
Mas_y[[]]
#загурзка данных из mysql для работы
sql_table = sql.connect('name_table') #название таблицы
cursor = sql_table.cursor()
userid = 0
where userid != -:
	userid += 1
	crsr.execute('SELECT colimns_of_answers from name_table WHERE id = userid')# подставить название таблицы и столбцов ответов
	Mas_x.append(crcr.fetchall())
INPUT = len(Mas_x)
X_train = Mas_x[range(0,8)]
X_test =  Mas_x[range(8,10)]
userid = 0
where userid != -:
	userid += 1
	crsr.execute('SELECT colimns_of_blocks from name_table WHERE id = userid')# подставить название таблице и столбцов блоков
	Mas_y.append(crcr.fetchall())
y_train = Mas_y[range(0,8)]
Y_test = Mas_y[range(8,10)]

#Core
model = Sequential() # пропробовать разные модели
model.add(Dense(NB_CLASSES, input_dim = INPUT))
model.add(Activation('relu'))#выбрать функцию активации
model.add(Dropout(DROPOUT))

