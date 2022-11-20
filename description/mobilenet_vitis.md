## CNN Architecture MobileNet

This is a re-implementation of MobileNet as described in [1] changed to fulfill hardware constraints of the Vitis AI framework for inference on Xilinx FPGAs.

Pretrained weights are available from the model database as follows:

- **ImageNet (with top layers)**: imagenet_mobilenet.h5
- **ImageNet (without top layers)**: imagenet_mobilenet_notop.h5

**Source file**: `/models/mobilenet_vitis.py`

## Usage:

```python
models.mobilenet_vitis.mobilenet_vitis(
    input_tensor=None, 
    include_top=True, 
    weight_path=None, 
    return_tensor=False, 
    classes=1000, 
    classifier_activation="softmax",
    alpha=1.0, 
    depth_multiplier=1
)
```

#### Arguments:
* **input_tensor**: optional keras layer, like an input tensor. 
* **include_top**: whether to include the top layers or top. 
* **weight_path**: If not none, these weights will be loaded. 
* **return_tensor**: Whether to return the network as tensor or as `tf.keras.model` (if true, weights will not be loaded). 
* **classes**: By default the number of classes are 1000 (ImageNet). Only important `include_top=True`. 
* **classifier_activation**: By default softmax (ImageNet). Only important if `include_top=True`.
* **alpha** (float, optional): controls the width of the network.
            - If `alpha` < 1.0, proportionally decreases the number
                of filters in each layer.
            - If `alpha` > 1.0, proportionally increases the number
                of filters in each layer.
            - If `alpha` = 1, default number of filters from the paper
                 are used at each layer. 
* depth_multiplier (int, optional): The number of depthwise convolution output channels
            for each input channel. Defaults to 1.

#### Returns:
The CNN architecture as `tf.keras.model` if `return_tensor=False`, otherwise as `tf.keras.layers`.

## References:
[1]	A. G. Howard et al., “[MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861),” 2017.<br/>
[2]	O. Russakovsky et al., “[ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575),” International Journal of Computer Vision (IJCV), vol. 115, no. 3, pp. 211–252, 2015, doi: 10.1007/s11263-015-0816-y.
