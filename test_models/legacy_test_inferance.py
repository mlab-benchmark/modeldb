import numpy as np
import sys
import os

from utils import model_load
from tensorflow.keras.preprocessing import image
from yaml import safe_load, YAMLError


#    Gewichte: http://tum4.icaml.org/weights/
#    Datensets: http://tum4.icaml.org/rs_data/

class cfg:
    weight_store = "./tmp"
    ds_store = "./tmp"


weightdb = [
    "imagenet_densenet121.h5",
    "imagenet_densenet121_notop.h5",
    "imagenet_densenet169.h5",
    "imagenet_densenet169_notop.h5",
    "imagenet_densenet201.h5",
    "imagenet_densenet201_notop.h5",
    "imagenet_mobilenet.h5",
    "imagenet_mobilenet_notop.h5",
    "imagenet_resnet50.h5",
    "imagenet_resnet50_notop.h5",
    "imagenet_resnet101.h5",
    "imagenet_resnet101_notop.h5",
    "imagenet_resnet152.h5",
    "imagenet_resnet152_notop.h5",
    "imagenet_vgg16.h5",
    "imagenet_vgg16_notop.h5",
    "imagenet_vgg19.h5",
    "imagenet_vgg19_notop.h5"]


def mlab_getweight(x):
    outfile = "%s/%s" % (cfg.weight_store, x)
    if os.path.exists(outfile):
        print("Using cached file %s" % outfile)
        return outfile
    url = '%s/weights/%s' % (cfg.baseurl, x)
    os.system("curl -u '%s:%s' -o %s %s" % (cfg.httpauth[0], cfg.httpauth[1], outfile, url))

    # This is not only slow, but as well a bit hacky
    #    r = requests.get(url, auth=cfg.httpauth)
    #    if r.status_code == 200:
    #        with open(outfile, 'wb') as out:
    #            for bits in r.iter_content():
    #                out.write(bits)

    return outfile


from matplotlib import pyplot as plt

if __name__ == "__main__":
    try:
        with open("credentials.yaml", 'r') as stream:
            cred = safe_load(stream)
    except FileNotFoundError as e:
        print(e)
        print("Filed loading credentials for webpage", )
        exit()

    cfg.httpauth = (cred["User"], cred["Pwd"])
    cfg.baseurl = cred["Url"]

    m = "imagenet-vgg19_vitis.h5"
    print("Downloading Weights %s" % (m))
    modelname = m.split(".")[0].split("-")[1]
    print("Model detected : <%s>" % modelname)
    weightfile = mlab_getweight(m)
    model = model_load("%s.py" % modelname)(include_top=True, weight_path=weightfile)
    print(model.summary())

    img = image.load_img("testdata/Walking_tiger_female.jpg", target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)[0]

    plt.bar(range(len(prediction)), prediction)
    plt.show()
    print("Predicted Class: %d" % (np.argmax(prediction)))
