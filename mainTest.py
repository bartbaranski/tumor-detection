import cv2
from keras._tf_keras.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('tumor10EpCat.h5')


image = cv2.imread('pred/pred48.jpg')


img = Image.fromarray(image)

img = img.resize((64, 64))

img = np.array(img)

input_img = np.expand_dims(img, axis=0)

result = model.predict(input_img)
result_final=np.argmax(result,axis=1)
print(result)
print(result_final)
if result_final == 0:
    print("Brak guza (NO).")
else:
    print("Guz (YES).")



