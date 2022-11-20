# CNN Architecture ResNet101

This is a re-implementation of ResNet101 as described [1] (Configuration: option B has been used) changed to fulfill
hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as follows:

- **ImageNet (with top layers)**: imagenet_resnet101.h5
- **ImageNet (without top layers)**: imagenet_resnet101_notop.h5

**Source file**: `/models/resnet101_vitis.py`

## Usage:

```python
models.resnet101_vitis.resnet101_vitis(
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
[1] K. He, X. Zhang, S. Ren and J. Sun, "[Deep Residual Learning for Image Recognition](https://doi.org/10.1109/CVPR.2016.90)," 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770-778, doi: 10.1109/CVPR.2016.90.<br/>
[2]	O. Russakovsky et al., “[ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575),” International Journal of Computer Vision (IJCV), vol. 115, no. 3, pp. 211–252, 2015, doi: 10.1007/s11263-015-0816-y.
