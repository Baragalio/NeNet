#первый коммит
from keras.models import load_model

print ('Begin')
print(1)
print("Vostrikova add")
print("Teselkin add")

model = load_model('model.h5')
def prediction(registration_data):
	output = model.predict(registration_data)
	return output
