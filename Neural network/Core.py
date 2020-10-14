
import numpy as np
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

#загурзка данных из mysql для работы
X_train =
y_train =
X_test =
Y_test =

#Core
model = Sequential() # пропробовать разные модели
model.add(Dense(NB_CLASSES, input_dim = INPUT))
model.add(Activation('relu'))#выбрать функцию активации
model.add(Dropout(DROPOUT))

