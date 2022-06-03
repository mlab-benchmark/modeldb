import tensorflow as tf;
import numpy as np
from models.vgg16_vitis import vgg16_vitis
from tensorflow.keras.preprocessing import image


if __name__=="__main__":
    model = vgg16_vitis(weight_path="/tmp/imagenet_vgg16.h5")
    print(model.summary())
    img = image.load_img("testdata/fish.jpeg", target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    print(prediction)

    

