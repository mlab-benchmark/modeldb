# densenet121_vitis

This is a re-implementation of VGG16 as decribed in Table 1 ConvNet Configuration D [1] changed to fulfill
hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as followss

- **imagenet_densenet121.h5:** /weights/imagenet_densenet121.h5 
- **imagenet_densenet121_notop.h5:** /weights/imagenet_densenet121_notop.h5


## References:
1. Huang, G., Liu, Z., Van Der Maaten, L. and Weinberger, K.Q., 2017. Densely connected convolutional networks. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 4700-4708).
2. Deng, J., Dong, W., Socher, R., Li, L.J., Li, K. and Fei-Fei, L., 2009, June. Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition (pp. 248-255). Ieee.