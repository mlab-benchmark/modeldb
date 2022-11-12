# Neural Network Architectures

This folder contains implementations for the following convolutional neural networks.

| Name              | Architecture | Source Publication                             | Weights  |
|-------------------|:------------:|------------------------------------------------|:--------:|
| vgg16_vitis       |    VGG16     | [Paper](https://arxiv.org/abs/1409.1556)       | ImageNet |
| vgg19_vitis       |    VGG19     | [Paper](https://arxiv.org/abs/1409.1556)       | ImageNet |
| resnet34_vitis    |   ResNet34   | [Paper](https://doi.org/10.1109/CVPR.2016.90)  |          |
| resnet50_vitis    |   ResNet50   | [Paper](https://doi.org/10.1109/CVPR.2016.90)  | ImageNet |
| resnet101_vitis   |  ResNet101   | [Paper](https://doi.org/10.1109/CVPR.2016.90)  | ImageNet |
| resnet152_vitis   |  ResNet152   | [Paper](https://doi.org/10.1109/CVPR.2016.90)  | ImageNet |
| densenet121_vitis | DenseNet121  | [Paper](https://doi.org/10.1109/CVPR.2017.243) | ImageNet |
| densenet161_vitis | DenseNet161  | [Paper](https://doi.org/10.1109/CVPR.2017.243) |          |
| densente169_vitis | DenseNet169  | [Paper](https://doi.org/10.1109/CVPR.2017.243) | ImageNet |
| densenet201_vitis | DenseNet201  | [Paper](https://doi.org/10.1109/CVPR.2017.243) | ImageNet |
| mobilenet_vitis   |  MobileNet   | [Paper](https://arxiv.org/abs/1704.04861)      | ImageNet |

**Hardware:** All models are FPGA ready and tested on an [AMD Xilinx ZCU102](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html) using [VitisAI](https://github.com/Xilinx/Vitis-AI).

For detail information, checkout the documentation [here](../description/)
