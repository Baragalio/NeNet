
import numpy as np
#import _sqlite3 as sql
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD , Adam
from keras.models import load_model
from keras.utils import np_utils, to_categorical

model = load_model('model.h5')

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
	print(reg_data_2)
	output = model.predict(reg_data_2)
	return output

#data2 = [2,1,3,2,1,3,1]
#h32 = prediction(data2)
#print(h32)