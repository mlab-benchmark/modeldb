<h1 align="center"> MLAB Model Library </h1> <br>

This repository is part of the project *Commercial off-the-shelf Inference Processor ML Benchmark* (MLAB) and includes a FPGA capable convolutional neural network library using TensorFlow.

## Model Library Overview
<!--
- **vgg16_vitis**: Vitis AI capable version of VGG16 [Doc](description/vgg16_vitis.md) [Src](description/vgg16_vitis.py)
- **vgg19_vitis**: Vitis AI capable version of VGG16 [Doc](description/vgg19_vitis.md) [Src](description/vgg19_vitis.py)
- **resnet50_vitis**: Vitis AI capable version of VGG16 [Doc](description/resnet50_vitis.md) [Src](description/resnet50_vitis.py)
- **resnet101_vitis**: Vitis AI capable version of VGG16 [Doc](description/resnet101_vitis.md) [Src](description/resnet101_vitis.py)
- **resnet152_vitis**: Vitis AI capable version of VGG16 [Doc](description/resnet152_vitis.md) [Src](description/resnet152_vitis.py)
- **densenet121_vitis**: Vitis AI capable version of VGG16 [Doc](description/densenet121_vitis.md) [Src](description/densenet121_vitis.py)
- **densenet169_vitis**: Vitis AI capable version of VGG16 [Doc](description/densenet169_vitis.md) [Src](description/densenet169_vitis.py)
- **densenet201_vitis**: Vitis AI capable version of VGG16 [Doc](description/densenet201_vitis.md) [Src](description/densenet201_vitis.py)
- **mobilenet_vitis**: Vitis AI capable version of VGG16 [Doc](description/mobilenet_vitis.md) [Src](description/mobilenet_vitis.py)
-->

| Name              | Architecture | Documentation                           | Source                             | Source Publication                              | Weights  |
|-------------------|:------------:|-----------------------------------------|------------------------------------|-------------------------------------------------|:--------:|
| vgg16_vitis       |    VGG16     | [Doc](description/vgg16_vitis.md)       | [Src](models/vgg16_vitis.py)       | [Paper](https://arxiv.org/abs/1409.1556)        | ImageNet |
| vgg19_vitis       |    VGG19     | [Doc](description/vgg19_vitis.md)       | [Src](models/vgg19_vitis.py)       | [Paper](https://arxiv.org/abs/1409.1556)        | ImageNet |
| resnet34_vitis    |   ResNet34   | [Doc](description/resnet34_vitis.md)    | [Src](models/resnet34_vitis.py)    | [Paper](https://doi.org/10.1109/CVPR.2016.90)   |          |
| resnet50_vitis    |   ResNet50   | [Doc](description/resnet50_vitis.md)    | [Src](models/resnet50_vitis.py)    | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| resnet101_vitis   |  ResNet101   | [Doc](description/resnet101_vitis.md)   | [Src](models/resnet101_vitis.py)   | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| resnet152_vitis   |  ResNet152   | [Doc](description/resnet152_vitis.md)   | [Src](models/resnet152_vitis.py)   | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| densenet121_vitis | DenseNet121  | [Doc](description/densenet121_vitis.md) | [Src](models/densenet121_vitis.py) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| densenet161_vitis | DenseNet161  | [Doc](description/densenet161_vitis.md) | [Src](models/densenet161_vitis.py) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  |          |
| densenet161_vitis | DenseNet169  | [Doc](description/densenet161_vitis.md) | [Src](models/densenet161_vitis.py) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| densenet201_vitis | DenseNet201  | [Doc](description/densenet201_vitis.md) | [Src](models/densenet201_vitis.py) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| mobilenet_vitis   |  MobileNet   | [Doc](description/mobilenet_vitis.md)   | [Src](models/mobilenet_vitis.py)   | [Paper](https://arxiv.org/abs/1704.04861)       | ImageNet |

**Hardware:** All models are FPGA ready and are tested on an [AMD Xilinx ZCU102](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html) using [VitisAI](https://github.com/Xilinx/Vitis-AI).

## Requirements
* TensorFlow (version > 2.3)

## Model Usage
```python
import tensorflow as tf
from models.vgg16_vitis import vgg16_vitis as basemodel

new_inputs = tf.keras.layers.Input(shape=(224, 224, 3))
x = basemodel(new_inputs, include_top=False, return_tensor=True, weight_path=None)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(1000, activation="softmax", name="predictions")(x)

model = tf.keras.Model(new_inputs, x, name="TestModel")

# [...]
```

### Opening an issue
You can also post bug reports and requests in [GitHub issues](https://github.com/tum-bgd/mlab_modeldb/issues).

### License
[Apache License 2.0](LICENSE)
