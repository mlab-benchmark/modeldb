# Neural Network Architectures

This folder contains implementations for the following convolutional neural networks.

| Name              | Architecture | Documentation                              | Source Publication                              | Weights  |
|-------------------|:------------:|--------------------------------------------|-------------------------------------------------|:--------:|
| vgg16_vitis       |    VGG16     | [Doc](../description/vgg16_vitis.md)       | [Paper](https://arxiv.org/abs/1409.1556)        | ImageNet |
| vgg19_vitis       |    VGG19     | [Doc](../description/vgg19_vitis.md)       | [Paper](https://arxiv.org/abs/1409.1556)        | ImageNet |
| resnet34_vitis    |   ResNet34   | [Doc](../description/resnet34_vitis.md)    | [Paper](https://doi.org/10.1109/CVPR.2016.90)   |          |
| resnet50_vitis    |   ResNet50   | [Doc](../description/resnet50_vitis.md)    | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| resnet101_vitis   |  ResNet101   | [Doc](../description/resnet101_vitis.md)   | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| resnet152_vitis   |  ResNet152   | [Doc](../description/resnet152_vitis.md)   | [Paper](https://doi.org/10.1109/CVPR.2016.90)   | ImageNet |
| densenet121_vitis | DenseNet121  | [Doc](../description/densenet121_vitis.md) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| densenet161_vitis | DenseNet161  | [Doc](../description/densenet161_vitis.md) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  |          |
| densente169_vitis | DenseNet169  | [Doc](../description/densente169_vitis.md) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| densenet201_vitis | DenseNet201  | [Doc](../description/densenet201_vitis.md) | [Paper](https://doi.org/10.1109/CVPR.2017.243)  | ImageNet |
| mobilenet_vitis   |  MobileNet   | [Doc](../description/mobilenet_vitis.md)   | [Paper](https://arxiv.org/abs/1704.04861)       | ImageNet |

**Hardware:** All models are FPGA ready and tested on an [AMD Xilinx ZCU102](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html) using [VitisAI](https://github.com/Xilinx/Vitis-AI).

For detail information, checkout the documentation [here](../description/).
