# resnet152_vitis

This is a re-implementation of VGG16 as decribed in Table 1 ConvNet Configuration D [1] changed to fulfill
hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as followss

- **imagenet_resnet152.h5:** /weights/imagenet_resnet152.h5 
- **imagenet_resnet152_notop.h5:** /weights/imagenet_resnet152_notop.h5


## References:
1. Deep Residual Learning for Image Recognition: (https://arxiv.org/pdf/1512.03385.pdf)
He, K., Zhang, X., Ren, S. and Sun, J., 2016. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
2. Deng, J., Dong, W., Socher, R., Li, L.J., Li, K. and Fei-Fei, L., 2009, June. Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition (pp. 248-255). Ieee.
