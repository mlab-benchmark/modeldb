# vgg16_vitis

This is a re-implementation of VGG16 as decribed in Table 1 ConvNet Configuration D [1] changed to fulfill
hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as followss

- **imagenet_vgg16.h5**: This model pretrained on ImageNet

## References:
1. Very Deep Convolutional Networks for Large-Scale Image Recognition (https://arxiv.org/pdf/1409.1556.pdf)
2. ImageNet: A large-scale hierarchical image database (https://ieeexplore.ieee.org/document/5206848)