# CNN Architecture VGG19

This is a re-implementation of VGG19 as described in Table 1 ConvNet Configuration D [1] changed to fulfill
hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as follows:

- **ImageNet (with top layers)**: imagenet_vgg19.h5
- **ImageNet (without top layers)**: imagenet_vgg19_notop.h5

**Source file**: `/models/vgg19_vitis.py`

## Usage:

```python
models.vgg19_vitis.vgg19_vitis(
    input_tensor=None, 
    include_top=True, 
    weight_path=None, 
    return_tensor=False, 
    classes=1000, 
    classifier_activation="softmax"
)
```

#### Arguments:
* **input_tensor**: optional keras layer, like an input tensor. 
* **include_top**: whether to include the top layers or top. 
* **weight_path**: If not none, these weights will be loaded. 
* **return_tensor**: Whether to return the network as tensor or as `tf.keras.model` (if true, weights will not be loaded). 
* **classes**: By default the number of classes are 1000 (ImageNet). Only important `include_top=True`. 
* **classifier_activation**: By default softmax (ImageNet). Only important if `include_top=True`.

#### Returns:
The CNN architecture as `tf.keras.model` if `return_tensor=False`, otherwise as `tf.keras.layers`.

## References:
[1] K. Simonyan and A. Zisserman, “[Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556.pdf),” in International Conference on Learning Representations, 2015.<br/>
[2]	O. Russakovsky et al., “[ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575),” International Journal of Computer Vision (IJCV), vol. 115, no. 3, pp. 211–252, 2015, doi: 10.1007/s11263-015-0816-y.
