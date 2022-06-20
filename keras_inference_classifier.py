import tensorflow as tf;
import numpy as np
from tensorflow.keras.preprocessing import image
import os
import importlib.util
import sys

# drop warnings (noisy, should not be a problem, change if debugging)
# -W ignore:DeprecationWarning

def test_model_load(x):
    modulename=x.split(".")[0]

    spec = importlib.util.spec_from_file_location(modulename, "models/%s" % (x))
    mod = importlib.util.module_from_spec(spec)
    
    sys.modules[modulename] = mod
    spec.loader.exec_module(mod)
    return mod.__dict__[modulename] # this is the generator function


if __name__=="__main__":
    # let us check for models available
    modx = [x for x in os.listdir("models") if x.endswith(".py")]
    for x in modx:
        m = test_model_load(x)()
        print(m.summary())
        

#from models.vgg16_vitis import vgg16_vitis 
##
##    
##    model = vgg16_vitis(weight_path="/tmp/imagenet_vgg16.h5")
##    print(model.summary())
##    img = image.load_img("testdata/fish.jpeg", target_size=(224, 224))
##    img_array = image.img_to_array(img)
##    img_batch = np.expand_dims(img_array, axis=0)
##    prediction = model.predict(img_batch)
##    print(prediction)
##
    

